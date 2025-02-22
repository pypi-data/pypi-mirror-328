import networkx as nx
import numpy as np
from typing import List, Dict, Tuple, Set
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import SpectralClustering
from collections import defaultdict
import spacy
from sentence_transformers import SentenceTransformer, util
import logging
import os
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.console import Console
from rich.logging import RichHandler
from pathlib import Path

# Set up rich console
console = Console()

# Set up logging with rich handler and SRSWTI watermark
log_dir = Path(__file__).parent.parent.parent / "logs"
log_dir.mkdir(exist_ok=True)
log_file = log_dir / "srswti_graph_merge.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [SRSWTI] %(message)s",
    handlers=[
        RichHandler(rich_tracebacks=True, console=console),
        logging.FileHandler(log_file)
    ]
)

logger = logging.getLogger("srswti_graph_merge")

class SRSWTIGraphFlow:
    """
    Enhanced graph-based document merging with hierarchical structure,
    multiple similarity metrics, and flow-based ordering.
    """
    def __init__(self, 
                 embedding_model: str = 'srswti-neural-embedder-v1',
                 spacy_model: str = 'en_core_web_sm'):
        console.print("[bold green][SRSWTI][/bold green] Initializing Enhanced Graph Merger...")
        model_mapping = {
            'srswti-neural-embedder-v1': 'all-MiniLM-L6-v2'
        }
        embedding_model = model_mapping.get(embedding_model, embedding_model)
        self.encoder = SentenceTransformer(embedding_model)
        self.nlp = spacy.load(spacy_model)
        self.tfidf = TfidfVectorizer(stop_words='english')
        logger.info("SRSWTI Graph Merger initialized successfully")
        
    def _calculate_edge_weights(self, doc1: str, doc2: str, 
                              emb1: np.ndarray, emb2: np.ndarray) -> Dict[str, float]:
        """Calculate multiple similarity metrics between documents."""
        weights = {}
        
        # Remove the Progress bar from this method since it's called within another Progress context
        # 1. Semantic similarity using embeddings
        weights['semantic'] = float(util.cos_sim(emb1, emb2))
        
        # 2. TF-IDF similarity
        tfidf_matrix = self.tfidf.fit_transform([doc1, doc2])
        weights['tfidf'] = float((tfidf_matrix @ tfidf_matrix.T).toarray()[0][1])
        
        # 3. Named entity overlap
        doc1_ents = set(ent.text.lower() for ent in self.nlp(doc1).ents)
        doc2_ents = set(ent.text.lower() for ent in self.nlp(doc2).ents)
        weights['entity'] = len(doc1_ents & doc2_ents) / max(1, len(doc1_ents | doc2_ents))
        
        # 4. Key phrase overlap using noun chunks
        doc1_chunks = set(chunk.text.lower() for chunk in self.nlp(doc1).noun_chunks)
        doc2_chunks = set(chunk.text.lower() for chunk in self.nlp(doc2).noun_chunks)
        weights['keyphrase'] = len(doc1_chunks & doc2_chunks) / max(1, len(doc1_chunks | doc2_chunks))
        
        # Combined weight with empirically determined coefficients
        weights['combined'] = (
            0.4 * weights['semantic'] +
            0.3 * weights['tfidf'] +
            0.2 * weights['entity'] +
            0.1 * weights['keyphrase']
        )
        
        logger.debug(f"SRSWTI Edge weights calculated: {weights}")
        return weights

    def _build_hierarchical_graph(self, documents: List[str]) -> Tuple[nx.Graph, nx.Graph, nx.Graph]:
        """Build multi-level graph structure."""
        console.print("[bold blue][SRSWTI][/bold blue] Building hierarchical document graph...")
        
        with Progress(console=console) as progress:
            # Encode all documents once
            task1 = progress.add_task("[cyan]Encoding documents...", total=len(documents))
            embeddings = self.encoder.encode(documents)
            progress.update(task1, completed=len(documents))
            
            # Level 3: Document-level graph
            logger.info("SRSWTI: Building document-level graph (Level 3)")
            doc_graph = nx.Graph()
            task2 = progress.add_task("[cyan]Building document graph...", total=len(documents))
            
            for i in range(len(documents)):
                doc_graph.add_node(i, text=documents[i], level='document')
                for j in range(i + 1, len(documents)):
                    weights = self._calculate_edge_weights(
                        documents[i], documents[j],
                        embeddings[i], embeddings[j]
                    )
                    if weights['combined'] > 0.3:  # Threshold for document connection
                        doc_graph.add_edge(i, j, **weights)
                progress.update(task2, advance=1)
            
            # Level 2: Paragraph-level graph
            logger.info("SRSWTI: Building paragraph-level graph (Level 2)")
            para_graph = nx.Graph()
            para_to_doc = {}  # Map paragraphs to their documents
            para_idx = 0
            
            task3 = progress.add_task("[cyan]Building paragraph graph...", total=len(documents))
            
            for doc_idx, doc in enumerate(documents):
                paragraphs = [p.strip() for p in doc.split('\n\n') if p.strip()]
                for para in paragraphs:
                    para_graph.add_node(para_idx, text=para, level='paragraph')
                    para_to_doc[para_idx] = doc_idx
                    para_idx += 1
                progress.update(task3, advance=1)
            
            # Level 1: Sentence-level graph
            logger.info("SRSWTI: Building sentence-level graph (Level 1)")
            sent_graph = nx.Graph()
            sent_to_para = {}
            sent_idx = 0
            
            task4 = progress.add_task("[cyan]Building sentence graph...", total=para_idx)
            
            for para_idx, para in para_graph.nodes(data='text'):
                sentences = [sent.text.strip() for sent in self.nlp(para).sents]
                for sent in sentences:
                    sent_graph.add_node(sent_idx, text=sent, level='sentence')
                    sent_to_para[sent_idx] = para_idx
                    sent_idx += 1
                progress.update(task4, advance=1)
        
        logger.info(f"SRSWTI Graph Statistics - Documents: {len(doc_graph)}, Paragraphs: {len(para_graph)}, Sentences: {len(sent_graph)}")
        return doc_graph, para_graph, sent_graph

    def _detect_communities(self, graph: nx.Graph, n_clusters: int = None) -> List[Set[int]]:
        """Enhanced community detection using spectral clustering and fallbacks."""
        console.print("[bold yellow][SRSWTI][/bold yellow] Detecting document communities...")
        
        if not graph.nodes():
            logger.warning("SRSWTI: Empty graph provided for community detection")
            return []
            
        if n_clusters is None:
            n_clusters = min(max(2, len(graph) // 5), 10)
            
        # First try: Connected components as a basic check
        components = list(nx.connected_components(graph))
        if len(components) > 1:
            logger.info(f"SRSWTI: Found {len(components)} disconnected components")
            communities = []
            for component in components:
                subgraph = graph.subgraph(component)
                if len(component) > n_clusters:
                    communities.extend(self._spectral_cluster_component(subgraph, n_clusters))
                else:
                    communities.append(component)
            return communities
        
        logger.info("SRSWTI: Graph is fully connected, applying spectral clustering")
        return self._spectral_cluster_component(graph, n_clusters)

    def _spectral_cluster_component(self, graph: nx.Graph, n_clusters: int) -> List[Set[int]]:
        """Apply spectral clustering to a connected component."""
        try:
            console.print("[bold magenta][SRSWTI][/bold magenta] Applying spectral clustering...")
            adj_matrix = nx.to_numpy_array(graph, weight='combined')
            
            clustering = SpectralClustering(
                n_clusters=min(n_clusters, len(graph) - 1),
                affinity='precomputed',
                random_state=42
            )
            labels = clustering.fit_predict(adj_matrix)
            
            communities = defaultdict(set)
            nodes = list(graph.nodes())
            for node_idx, label in enumerate(labels):
                communities[label].add(nodes[node_idx])
            
            logger.info(f"SRSWTI: Successfully identified {len(communities)} communities")
            return list(communities.values())
            
        except Exception as e:
            logger.error(f"SRSWTI Spectral clustering failed: {e}")
            return [set(graph.nodes())]

    def _order_by_centrality_flow(self, graph: nx.Graph, community: Set[int]) -> List[int]:
        """Order nodes within community using centrality and flow."""
        if not community:
            return []
            
        console.print("[bold cyan][SRSWTI][/bold cyan] Ordering nodes by centrality and flow...")
        subgraph = graph.subgraph(community)
        
        try:
            centrality = {}
            # Remove the Progress bar and process directly
            for node in subgraph.nodes():
                measures = []
                measures.append(nx.pagerank(subgraph, weight='combined').get(node, 0))
                measures.append(nx.degree_centrality(subgraph).get(node, 0))
                
                if nx.is_connected(subgraph) and len(subgraph) > 2:
                    try:
                        if len(subgraph) < 500:
                            measures.append(nx.eigenvector_centrality(
                                subgraph, 
                                weight='combined',
                                max_iter=1000,
                                tol=1e-6
                            ).get(node, 0))
                        else:
                            measures.append(nx.eigenvector_centrality_numpy(
                                subgraph, 
                                weight='combined'
                            ).get(node, 0))
                    except:
                        measures.append(0)
                
                centrality[node] = sum(measures) / len(measures)
            
            ordered = [max(centrality.items(), key=lambda x: x[1])[0]]
            remaining = set(community) - {ordered[0]}
            
            logger.info("SRSWTI: Ordering nodes by flow similarity")
            while remaining:
                last = ordered[-1]
                next_node = max(
                    remaining,
                    key=lambda n: (
                        graph[last][n]['combined'] if graph.has_edge(last, n) else 0
                    ) + centrality[n]
                )
                ordered.append(next_node)
                remaining.remove(next_node)
            
            return ordered
            
        except Exception as e:
            logger.error(f"SRSWTI Centrality-based ordering failed: {e}")
            return list(community)

    def merge_documents(self, documents: List[str]) -> List[str]:
        """Main method to merge documents using enhanced graph-based approach."""
        console.print("\n[bold green]=== SRSWTI Document Merger Started ===[/bold green]\n")
        
        doc_graph, para_graph, sent_graph = self._build_hierarchical_graph(documents)
        doc_communities = self._detect_communities(doc_graph)
        
        merged_documents = []
        with Progress(console=console) as progress:
            task = progress.add_task("[cyan]Merging document communities...", total=len(doc_communities))
            
            for community in doc_communities:
                if len(community) < 2:
                    merged_documents.append(documents[list(community)[0]])
                    progress.update(task, advance=1)
                    continue
                
                ordered_docs = self._order_by_centrality_flow(doc_graph, community)
                merged_text = []
                current_topic = None
                
                for doc_idx in ordered_docs:
                    doc_text = documents[doc_idx]
                    doc_paras = [
                        idx for idx, data in para_graph.nodes(data=True)
                        if data['text'] in doc_text
                    ]
                    
                    ordered_paras = self._order_by_centrality_flow(para_graph, set(doc_paras))
                    
                    for para_idx in ordered_paras:
                        para_text = para_graph.nodes[para_idx]['text']
                        doc = self.nlp(para_text)
                        topic_entities = {ent.text for ent in doc.ents if ent.label_ in {'ORG', 'PRODUCT', 'GPE'}}
                        
                        if topic_entities and current_topic != topic_entities:
                            current_topic = topic_entities
                            merged_text.append(para_text)
                        else:
                            merged_text.append(para_text)
                
                merged_documents.append('\n\n'.join(merged_text))
                progress.update(task, advance=1)
        
        console.print("\n[bold green]=== SRSWTI Document Merger Completed ===[/bold green]\n")
        logger.info(f"SRSWTI: Successfully merged {len(documents)} documents into {len(merged_documents)} outputs")
        return merged_documents

def main():
    # Sample test documents with more diverse and extensive content
    test_documents = [
        """Blockchain technology is revolutionizing financial transactions.
        Decentralized ledgers provide transparent and secure record-keeping.
        Smart contracts enable automated, trustless financial agreements.""",
        
        """Cryptocurrency markets are evolving with advanced blockchain technologies.
        Bitcoin and Ethereum represent major innovations in digital finance.
        Blockchain is creating new paradigms for monetary exchange.""",
        
        """Artificial Intelligence is transforming blockchain applications.
        Machine learning algorithms enhance blockchain security and efficiency.
        AI-powered smart contracts can adapt and learn from transaction patterns.""",
        
        """Autonomous vehicles are integrating blockchain for secure data management.
        Vehicle-to-vehicle communication relies on decentralized blockchain networks.
        Blockchain ensures transparent and tamper-proof automotive data tracking.""",
        
        """Self-driving car technologies are advancing rapidly.
        Machine learning enables complex navigation and decision-making algorithms.
        Autonomous vehicles are becoming more sophisticated and reliable.""",
        
        """Electric vehicles are revolutionizing transportation infrastructure.
        AI-powered systems optimize battery performance and energy efficiency.
        Autonomous driving technologies are reducing human error in transportation.""",
        
        """Barbie dolls have evolved with modern technology and cultural awareness.
        Mattel is incorporating diverse representations in doll design.
        Collectible and limited edition Barbie dolls reflect contemporary social trends.""",
        
        """Barbie as a brand is exploring technological integration.
        Smart dolls with interactive features are becoming more popular.
        Augmented reality experiences are enhancing traditional doll play.""",
        
        """AI is influencing toy design and manufacturing.
        Personalized Barbie dolls can now be customized with advanced 3D printing.
        Machine learning helps create more inclusive and representative doll collections.""",
        
        """Blockchain technology could revolutionize toy authentication and collectibles.
        Digital certificates can verify the authenticity of rare Barbie dolls.
        Decentralized platforms enable secure trading of collectible toys."""
    ]
    # Optional testing configurations
    verbose_testing = True
    max_merge_iterations = 3

    try:
        # Initialize the merger
        merger = SRSWTIGraphFlow()
        
        # Merge the documents
        console.print("\n[bold blue]Testing document merger with sample texts...[/bold blue]\n")
        merged_docs = merger.merge_documents(test_documents)
        
        # Print results
        console.print("\n[bold green]Merged Documents:[/bold green]")
        for i, doc in enumerate(merged_docs, 1):
            console.print(f"\n[cyan]Merged Document {i}:[/cyan]")
            console.print(doc)
            console.print("\n" + "-"*50)
            
    except Exception as e:
        logger.error(f"Error during testing: {e}")
        raise

if __name__ == "__main__":
    main()