from typing import List, Dict, Optional, Union, Tuple

import numpy as np
from abc import ABC, abstractmethod
from typing import List, Dict, Union, Tuple, Optional
from sklearn.metrics import calinski_harabasz_score
class DocumentProcessor(ABC):
    """Base class for document processing operations."""
    @abstractmethod
    def process(self):
        pass
from sentence_transformers import SentenceTransformer, util
import nltk
from nltk.tokenize import sent_tokenize
import numpy as np
from sklearn.cluster import AgglomerativeClustering, KMeans
import spacy
from collections import defaultdict
from itertools import combinations
import logging
import networkx as nx
import subprocess



# Lazy import of heavy libraries
def lazy_import(library):
    """Lazily import libraries to reduce initial memory load."""
    try:
        if library == 'sentence_transformers':
            from sentence_transformers import SentenceTransformer, util
            return SentenceTransformer, util
        elif library == 'nltk':
            import nltk
            return nltk
        elif library == 'spacy':
            import spacy
            spacy.cli.download("en_core_web_sm")
            return spacy
        elif library == 'sklearn':
            from sklearn.cluster import AgglomerativeClustering
            from sklearn.decomposition import NMF
            from sklearn.feature_extraction.text import TfidfVectorizer
            return AgglomerativeClustering, NMF, TfidfVectorizer
        elif library == 'networkx':
            import networkx as nx
            return nx
    except ImportError as e:
        logging.error(f"Could not import {library}: {e}")
        return None

class SRSWTIPureFlow(DocumentProcessor):
    """
    Handles document and text merging using various strategies:
    1. Semantic similarity based merging
    2. Sequential merging with coherence optimization
    3. Hierarchical clustering based merging
    4. Graph-based merging
    5. Topic-based merging
    """
    
    def __init__(self, 
                 embedding_model: str = 'all-MiniLM-L6-v2',
                 language: str = 'en',
                 spacy_model: str = 'en_core_web_sm'):
        """
        Initialize the merger with specified models.
        
        Args:
            embedding_model: SentenceTransformer model for embeddings
            language: Language for text processing
            spacy_model: Spacy model for linguistic analysis
        """
        self.embedding_model = embedding_model
        self.language = language
        self.spacy_model = spacy_model
        
        # Lazy loaded attributes
        self._encoder = None
        self._nlp = None

    @property
    def encoder(self):
        """Lazy load sentence transformer"""
        if self._encoder is None:
            SentenceTransformer, _ = lazy_import('sentence_transformers')
            if SentenceTransformer:
                self._encoder = SentenceTransformer(self.embedding_model)
        return self._encoder
    
    @property
    def nlp(self):
        """Lazy load spacy model"""
        if self._nlp is None:
            spacy = lazy_import('spacy')
            if spacy:
                try:
                    self._nlp = spacy.load(self.spacy_model)
                except OSError:
                    logging.warning(f"Could not load spacy model {self.spacy_model}. Using default.")
                    self._nlp = spacy.load('en_core_web_sm')
        return self._nlp
    
    def _safe_download_nltk(self):
        """Safely download NLTK resources"""
        try:
            nltk = lazy_import('nltk')
            if nltk:
                nltk.download('punkt', quiet=True)
        except Exception as e:
            logging.error(f"NLTK download failed: {e}")
    
    def merge_by_similarity(self, 
                       documents: List[str],
                       threshold: float = 0.5,
                       strategy: str = 'clustering',
                       min_cluster_size: int = 2,
                       adaptive_threshold: bool = True) -> List[str]:
        """
        Enhanced similarity-based merging with proper distance handling.
        """
        try:
            embeddings = self.encoder.encode(documents)
            
            if adaptive_threshold:
                threshold = self._calculate_adaptive_threshold(documents, embeddings)
            
            if strategy == 'clustering':
                similarity_matrix = util.cos_sim(embeddings, embeddings)
                # Ensure distances are non-negative
                distances = np.clip(1 - similarity_matrix.numpy(), 0, 2)  # Clip to valid range
                
                n_docs = len(documents)
                if n_docs < 3:
                    return self._enhanced_pairwise_merge(documents, embeddings, threshold)
                
                min_clusters = max(2, n_docs // 5)
                max_clusters = min(n_docs - 1, 10)
                
                best_clusters = None
                best_score = -float('inf')
                
                # Try different clustering approaches
                clustering_methods = [
                    ('hierarchical', lambda n: AgglomerativeClustering(
                        n_clusters=n,
                        metric='euclidean',  # Changed from precomputed
                        linkage='ward'
                    )),
                    ('kmeans', lambda n: KMeans(
                        n_clusters=n,
                        random_state=42
                    ))
                ]
                
                for method_name, clusterer in clustering_methods:
                    for n_clusters in range(min_clusters, max_clusters + 1):
                        try:
                            if method_name == 'hierarchical':
                                labels = clusterer(n_clusters).fit_predict(embeddings)
                            else:
                                labels = clusterer(n_clusters).fit_predict(embeddings)
                            
                            if len(set(labels)) > 1:
                                # Use calinski_harabasz_score instead of silhouette
                                score = calinski_harabasz_score(embeddings, labels)
                                if score > best_score:
                                    best_score = score
                                    best_clusters = labels
                                    
                        except Exception as cluster_error:
                            logging.debug(f"{method_name} clustering failed for n_clusters={n_clusters}: {cluster_error}")
                            continue
                
                if best_clusters is None:
                    return self._enhanced_pairwise_merge(documents, embeddings, threshold)
                
                # Process clusters with improved ordering
                merged_docs = defaultdict(list)
                for doc_idx, cluster_idx in enumerate(best_clusters):
                    merged_docs[cluster_idx].append({
                        'text': documents[doc_idx],
                        'embedding': embeddings[doc_idx]
                    })
                
                final_docs = []
                for cluster_docs in merged_docs.values():
                    if len(cluster_docs) >= min_cluster_size:
                        # Order documents within cluster by similarity to cluster centroid
                        cluster_embs = np.array([doc['embedding'] for doc in cluster_docs])
                        centroid = np.mean(cluster_embs, axis=0)
                        similarities = np.dot(cluster_embs, centroid)
                        ordered_indices = np.argsort(-similarities)
                        
                        ordered_texts = [cluster_docs[i]['text'] for i in ordered_indices]
                        final_docs.append(self._merge_text_group(ordered_texts))
                    else:
                        final_docs.extend(doc['text'] for doc in cluster_docs)
                
                return final_docs
                
            else:  # Pairwise strategy
                return self._enhanced_pairwise_merge(documents, embeddings, threshold)
                
        except Exception as e:
            logging.error(f"Similarity merging failed: {e}")
            return documents


    def _calculate_adaptive_threshold(self, 
                                    documents: List[str],
                                    embeddings: np.ndarray) -> float:
        """
        Calculate adaptive threshold based on document properties.
        """
        # Get document statistics
        doc_lengths = [len(doc.split()) for doc in documents]
        avg_length = np.mean(doc_lengths)
        length_std = np.std(doc_lengths)
        
        # Calculate average pairwise similarity
        similarity_matrix = util.cos_sim(embeddings, embeddings)
        avg_similarity = similarity_matrix.mean().item()
        
        # Adjust threshold based on document properties
        base_threshold = 0.5
        length_factor = 1 + 0.1 * (length_std / avg_length)  # Higher variance → higher threshold
        similarity_factor = 1 + 0.2 * (1 - avg_similarity)  # Lower average similarity → higher threshold
        
        return base_threshold * length_factor * similarity_factor

    def _enhanced_pairwise_merge(self,
                            documents: List[str],
                            embeddings: np.ndarray,
                            threshold: float) -> List[str]:
        """
        Enhanced pairwise merging with better pair selection.
        """
        merged = []
        used_indices = set()
        
        # Calculate all pairwise similarities
        similarity_matrix = util.cos_sim(embeddings, embeddings)
        pairs = []
        
        for i, j in combinations(range(len(documents)), 2):
            similarity = similarity_matrix[i][j].item()
            if similarity >= threshold:
                pairs.append((similarity, i, j))
        
        # Sort pairs by similarity
        pairs.sort(reverse=True)
        
        # Merge pairs in order of similarity
        for sim, i, j in pairs:
            if i not in used_indices and j not in used_indices:
                merged_text = self._merge_pair(documents[i], documents[j])
                merged.append(merged_text)
                used_indices.update([i, j])
        
        # Add remaining documents
        for i in range(len(documents)):
            if i not in used_indices:
                merged.append(documents[i])
        
        return merged
    
    def merge_sequential(self,
                        documents: List[str],
                        max_chunk_size: int = 1000,
                        overlap: bool = True) -> str:
        """
        Merge documents sequentially with optional overlap.
        
        Args:
            documents: List of documents to merge
            max_chunk_size: Maximum size of merged chunks
            overlap: Whether to maintain overlap between chunks
            
        Returns:
            Merged document
        """
        # Split into sentences
        all_sentences = []
        for doc in documents:
            sentences = sent_tokenize(doc)
            all_sentences.extend(sentences)
            
        if not overlap:
            return ' '.join(all_sentences)
            
        # Create overlapping chunks
        chunks = []
        current_chunk = []
        current_size = 0
        overlap_size = 2  # Number of sentences to overlap
        
        for sentence in all_sentences:
            sentence_size = len(sentence.split())
            
            if current_size + sentence_size > max_chunk_size:
                # Add chunk and keep overlap sentences
                chunks.append(' '.join(current_chunk))
                current_chunk = current_chunk[-overlap_size:]  # Keep overlap
                current_size = sum(len(s.split()) for s in current_chunk)
            
            current_chunk.append(sentence)
            current_size += sentence_size
            
        if current_chunk:
            chunks.append(' '.join(current_chunk))
            
        return '\n\n'.join(chunks)
    
    def merge_by_graph(self,
                  documents: List[str],
                  threshold: float = 0.7,
                  merge_communities: bool = True,
                  min_community_size: int = 2,
                  edge_weight_method: str = 'combined') -> List[str]:
        """
        Enhanced graph-based document merging.
        
        Args:
            documents: List of documents to merge
            threshold: Base similarity threshold
            merge_communities: Use community detection
            min_community_size: Minimum size for a community
            edge_weight_method: 'cosine', 'jaccard', or 'combined'
        """
        try:
            from .graph_merge import SRSWTIGraphFlow

            # Initialize enhanced graph merger
            merger = SRSWTIGraphFlow(
                embedding_model=self.embedding_model,
                spacy_model=self.spacy_model
            )
            
            # Use the enhanced merger if documents exist
            if documents:
                return merger.merge_documents(documents)
                
            return documents
            
        except Exception as e:
            logging.error(f"Enhanced graph merging failed: {e}")
            # Fallback to original implementation
            
            # Get embeddings and basic similarity
            embeddings = self.encoder.encode(documents)
            similarity_matrix = util.cos_sim(embeddings, embeddings)
            
            # Build enhanced graph
            G = nx.Graph()
            for i in range(len(documents)):
                # Add node with more metadata
                G.add_node(i, 
                        text=documents[i],
                        length=len(documents[i].split()),
                        embedding=embeddings[i])
            
            # Enhanced edge weight calculation
            for i, j in combinations(range(len(documents)), 2):
                weights = {}
                
                # Cosine similarity from embeddings
                weights['cosine'] = similarity_matrix[i][j].item()
                
                # Jaccard similarity for terms
                doc1_terms = set(documents[i].lower().split())
                doc2_terms = set(documents[j].lower().split())
                weights['jaccard'] = len(doc1_terms & doc2_terms) / len(doc1_terms | doc2_terms)
                
                # Entity overlap using spaCy
                doc1_ents = set(ent.text for ent in self.nlp(documents[i]).ents)
                doc2_ents = set(ent.text for ent in self.nlp(documents[j]).ents)
                weights['entity'] = len(doc1_ents & doc2_ents) / max(1, len(doc1_ents | doc2_ents))
                
                # Combined weight
                combined_weight = (weights['cosine'] * 0.5 + 
                                weights['jaccard'] * 0.3 + 
                                weights['entity'] * 0.2)
                
                if combined_weight >= threshold:
                    G.add_edge(i, j, 
                            weight=combined_weight,
                            weights=weights)
            
            if merge_communities:
                # Enhanced community detection
                communities = self._detect_communities(G, min_community_size)
                
                # Merge with ordering
                merged = []
                for community in communities:
                    if len(community) >= min_community_size:
                        community_docs = [documents[i] for i in community]
                        ordered_docs = self._order_documents(community_docs)
                        merged.append(self._merge_text_group(ordered_docs))
                    else:
                        # Add small communities as individual documents
                        for node in community:
                            merged.append(documents[node])
                            
                return merged
            
            return self._merge_components(G, documents)

    def _detect_communities(self, G: nx.Graph, min_size: int) -> List[set]:
        """
        Enhanced community detection with multiple algorithms.
        """
        # Try different community detection methods
        methods = {
            'louvain': nx.community.louvain_communities,
            'label_prop': nx.community.label_propagation_communities,
            'fluid': nx.community.asyn_fluidc
        }
        
        best_communities = None
        best_modularity = -1
        
        for method_name, method in methods.items():
            try:
                communities = list(method(G))
                modularity = nx.community.modularity(G, communities)
                
                if modularity > best_modularity:
                    best_modularity = modularity
                    best_communities = communities
            except Exception as e:
                logging.warning(f"Community detection failed for {method_name}: {e}")
        
        # Post-process communities
        if best_communities:
            return self._refine_communities(G, best_communities, min_size)
        
        # Fallback to connected components
        return list(nx.connected_components(G))

    def _refine_communities(self, G: nx.Graph, communities: List[set], min_size: int) -> List[set]:
        """
        Refine communities based on internal connectivity and size.
        """
        refined = []
        
        for community in communities:
            if len(community) < min_size:
                refined.append(community)
                continue
                
            # Check internal connectivity
            subgraph = G.subgraph(community)
            density = nx.density(subgraph)
            
            if density < 0.3:  # Low connectivity
                # Split based on internal structure
                sub_communities = list(nx.community.kernighan_lin_bisection(subgraph))
                refined.extend(sub_communities)
            else:
                refined.append(community)
        
        return refined

    def _order_documents(self, documents: List[str]) -> List[str]:
        """
        Order documents for coherent merging.
        """
        # Create similarity matrix
        embeddings = self.encoder.encode(documents)
        similarity_matrix = util.cos_sim(embeddings, embeddings)
        
        # Find optimal ordering using TSP-like approach
        n = len(documents)
        visited = {0}  # Start with first document
        ordered_indices = [0]
        
        while len(visited) < n:
            last_idx = ordered_indices[-1]
            next_idx = max(
                (i for i in range(n) if i not in visited),
                key=lambda i: similarity_matrix[last_idx][i]
            )
            visited.add(next_idx)
            ordered_indices.append(next_idx)
        
        return [documents[i] for i in ordered_indices]
    
    def merge_by_topic(self,
                      documents: List[str],
                      num_topics: int = 5) -> Dict[str, str]:
        """
        Merge documents by topic similarity.
        
        Args:
            documents: List of documents to merge
            num_topics: Number of topics to consider
            
        Returns:
            Dictionary of topic -> merged document
        """
        from sklearn.decomposition import NMF
        from sklearn.feature_extraction.text import TfidfVectorizer
        
        # Create document-term matrix
        vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
        dtm = vectorizer.fit_transform(documents)
        
        # Apply NMF for topic modeling
        nmf = NMF(n_components=num_topics, random_state=42)
        topic_matrix = nmf.fit_transform(dtm)
        
        # Assign documents to topics
        topic_docs = defaultdict(list)
        for idx, topic_weights in enumerate(topic_matrix):
            main_topic = topic_weights.argmax()
            topic_docs[main_topic].append(documents[idx])
            
        # Merge documents within each topic
        merged = {}
        feature_names = vectorizer.get_feature_names_out()
        
        for topic_idx, docs in topic_docs.items():
            # Get topic keywords
            topic_terms = [
                feature_names[i] 
                for i in nmf.components_[topic_idx].argsort()[:-10:-1]
            ]
            topic_name = f"Topic {topic_idx}: {', '.join(topic_terms[:3])}"
            merged[topic_name] = self._merge_text_group(docs)
            
        return merged
    
    def _merge_pair(self, doc1: str, doc2: str) -> str:
        """Merge two documents while maintaining coherence."""
        # Parse documents
        doc1_parsed = self.nlp(doc1)
        doc2_parsed = self.nlp(doc2)
        
        # Extract key information
        doc1_ents = set(ent.text for ent in doc1_parsed.ents)
        doc2_ents = set(ent.text for ent in doc2_parsed.ents)
        
        # If documents share entities, try to merge relevant sections
        if doc1_ents & doc2_ents:
            # Split into sentences
            sentences1 = [sent.text for sent in doc1_parsed.sents]
            sentences2 = [sent.text for sent in doc2_parsed.sents]
            
            # Find optimal arrangement
            merged_sentences = []
            used2 = set()
            
            for sent1 in sentences1:
                merged_sentences.append(sent1)
                # Find related sentence in doc2
                for i, sent2 in enumerate(sentences2):
                    if i not in used2:
                        sent_similarity = self.encoder.encode(
                            [sent1, sent2],
                            convert_to_tensor=True
                        )
                        if util.cos_sim(sent_similarity[0], sent_similarity[1]) > 0.7:
                            merged_sentences.append(sent2)
                            used2.add(i)
                            
            # Add remaining sentences from doc2
            for i, sent2 in enumerate(sentences2):
                if i not in used2:
                    merged_sentences.append(sent2)
                    
            return ' '.join(merged_sentences)
        
        # If no shared entities, concatenate with section break
        return f"{doc1}\n\n{doc2}"
    
    def _merge_text_group(self, texts: List[str]) -> str:
        """Merge a group of texts maintaining coherence."""
        if not texts:
            return ""
        if len(texts) == 1:
            return texts[0]
            
        # Start with first text
        merged = texts[0]
        
        # Iteratively merge with remaining texts
        for text in texts[1:]:
            merged = self._merge_pair(merged, text)
            
        return merged
    
    def process(self, 
                documents: List[str],
                method: str = 'similarity',
                **kwargs) -> Union[List[str], str, Dict[str, str]]:
        """
        Process documents according to DocumentProcessor interface.
        
        Args:
            documents: List of documents to merge
            method: 'similarity', 'sequential', 'graph', or 'topic'
            **kwargs: Additional arguments for specific methods
            
        Returns:
            Merged document(s) in format depending on method
        """
        if method == 'similarity':
            return self.merge_by_similarity(documents, **kwargs)
        elif method == 'sequential':
            return self.merge_sequential(documents, **kwargs)
        elif method == 'graph':
            return self.merge_by_graph(documents, **kwargs)
        elif method == 'topic':
            return self.merge_by_topic(documents, **kwargs)
        else:
            raise ValueError(f"Unknown merge method: {method}")

# Example usage
if __name__ == "__main__":
    # Sample documents covering diverse topics including sports, technology, cars, and edge cases
    documents = [
        "Machine learning is a subset of artificial intelligence. It focuses on data and algorithms.",
        "Trasnfomres are advanced robotic beings that can change their form. They originated in popular science fiction.",
        "Formula 1 racing represents the pinnacle of automotive engineering and high-performance technology.",
        "Amchine elarning enables advanced data analysis through complex neural network architectures.",
        "Lionel Messi's soccer career demonstrates the intersection of athletic skill and strategic decision-making.",
        "Electric vehicles are transforming the automotive industry. Tesla has been a pioneer in autonomous driving technology.",
        "The Mercedes-AMG Project One combines Formula 1 racing technology with road-legal hypercar design.",
        "Quantum computing represents a revolutionary approach to computational problem-solving.",
        "NBA analytics have transformed basketball strategy, using advanced statistical models to optimize player performance.",
        "Blockchain technology provides decentralized and secure transaction systems for sports memorabilia and athlete contracts.",
        "Autonomous vehicle navigation systems use complex machine learning algorithms similar to those in advanced sports analytics.",
        "Artificial intelligence is revolutionizing sports training, providing real-time performance insights and predictive modeling.",
        "Modern racing cars use advanced telemetry and machine learning to optimize vehicle performance and driver strategy.",
        "Extreme sports athletes increasingly use wearable technology and AI to analyze and improve their techniques.",
        "The convergence of technology and sports continues to push the boundaries of human performance and understanding."
    ]
    
    # Initialize merger
    merger = SRSWTIPureFlow()
    
    # Test different merge strategies
    similarity_merged = merger.process(documents, method='similarity')
    sequential_merged = merger.process(documents, method='sequential')
    graph_merged = merger.process(documents, method='graph')
    topic_merged = merger.process(documents, method='topic')
    
    # Print results
    print("Similarity-based merge:", similarity_merged)
    print("\nSequential merge:", sequential_merged)
    print("\nGraph-based merge:", graph_merged)
    print("\nTopic-based merge:", topic_merged)