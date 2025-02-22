from typing import List, Dict, Tuple, Optional
import numpy as np
from scipy.sparse import csr_matrix, vstack
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import spacy
from collections import Counter
import numpy as np
from rich.console import Console
from rich.panel import Panel
from rich.progress import track
from datetime import datetime
import logging
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [SRSWTI-IR] %(levelname)s: %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(os.path.dirname(__file__), 'srswti_ir.log')),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger('SRSWTI-IR')

class SRSWTISearchEngine:
    def __init__(self, embedding_model: str = 'srswti-neural-embedder-v1'):
        """Initialize search engine components"""
        logger.info("Initializing SRSWTI Search Engine components...")
        # Map SRSWTI model alias to the actual model
        model_mapping = {
            'srswti-neural-embedder-v1': 'all-mpnet-base-v2'
        }
        actual_model = model_mapping.get(embedding_model, embedding_model)
        self.embedder = SentenceTransformer(actual_model)
        self.nlp = spacy.load('en_core_web_sm')
        self.tfidf = TfidfVectorizer(ngram_range=(1, 2))
        self.bm25_k1 = 1.5
        self.bm25_b = 0.75
        logger.info("SRSWTI Search Engine initialized successfully")

        
    def preprocess_text(self, text: str) -> str:
        """SRSWTI Advanced Text Preprocessing Pipeline"""
        doc = self.nlp(text.lower())
        tokens = [
            token.lemma_ 
            for token in doc 
            if not token.is_stop and not token.is_punct
        ]
        logger.debug(f"SRSWTI Preprocessed text: {' '.join(tokens)}")
        return " ".join(tokens)
    
    def calculate_bm25_scores(self, query: str, documents: List[str]) -> np.ndarray:
        """SRSWTI BM25 Probabilistic Ranking Implementation"""
        logger.info("Running BM25 scoring...")
        
        # Preprocess documents
        processed_docs = []
        for doc in documents:
            processed_docs.append(self.preprocess_text(doc))
        processed_query = self.preprocess_text(query)
        
        # SRSWTI Mathematical Components
        tfidf_matrix = self.tfidf.fit_transform(processed_docs)
        doc_lengths = np.sum(tfidf_matrix > 0, axis=1).A1
        avg_doc_length = np.mean(doc_lengths)
            
        query_terms = processed_query.split()
        query_vector = self.tfidf.transform([processed_query])
        
        # SRSWTI Probabilistic Scoring
        scores = np.zeros(len(documents))
        feature_names = self.tfidf.get_feature_names_out()
        
        for term in query_terms:
            if term in feature_names:
                term_idx = feature_names.tolist().index(term)
                tf = tfidf_matrix[:, term_idx].toarray().flatten()
                idf = self.tfidf.idf_[term_idx]
                
                # SRSWTI BM25 Probabilistic Formula
                numerator = np.multiply(tf, (self.bm25_k1 + 1))
                denominator = tf + self.bm25_k1 * (1 - self.bm25_b + self.bm25_b * doc_lengths / avg_doc_length)
                scores += np.multiply(idf, (numerator / denominator).flatten())
                
        logger.info(f"SRSWTI BM25 scoring completed for {len(documents)} documents")
        return scores

    def hybrid_search(self, 
                     query: str, 
                     documents: List[str],
                     weights: Dict[str, float] = None) -> List[Tuple[int, float]]:
        """SRSWTI Hybrid Neural-Probabilistic Search"""
        if weights is None:
            weights = {'bm25': 0.4, 'semantic': 0.4, 'proximity': 0.2}
        
        logger.info("Starting hybrid search pipeline...")
        
        # SRSWTI BM25 Component
        bm25_scores = self.calculate_bm25_scores(query, documents)
        
        # SRSWTI Neural Component
        query_embedding = self.embedder.encode([query])[0]
        doc_embeddings = self.embedder.encode(documents)
        semantic_scores = cosine_similarity([query_embedding], doc_embeddings)[0]
        
        # SRSWTI Proximity Analysis
        proximity_scores = self.calculate_proximity_scores(query, documents)
        
        # SRSWTI Score Normalization
        bm25_scores = bm25_scores / np.max(bm25_scores) if np.max(bm25_scores) > 0 else bm25_scores
        semantic_scores = semantic_scores / np.max(semantic_scores) if np.max(semantic_scores) > 0 else semantic_scores
        proximity_scores = proximity_scores / np.max(proximity_scores) if np.max(proximity_scores) > 0 else proximity_scores
        
        # SRSWTI Score Fusion
        final_scores = (
            weights['bm25'] * bm25_scores +
            weights['semantic'] * semantic_scores +
            weights['proximity'] * proximity_scores
        )
        
        ranked_indices = np.argsort(-final_scores)
        logger.info("SRSWTI hybrid search completed successfully")
        return [(idx, final_scores[idx]) for idx in ranked_indices]
    
    def calculate_proximity_scores(self, query: str, documents: List[str]) -> np.ndarray:
        """SRSWTI Proximity Analysis Module"""
        query_terms = set(self.preprocess_text(query).split())
        scores = np.zeros(len(documents))
        
        for idx, doc in enumerate(documents):
            doc_tokens = self.preprocess_text(doc).split()
            positions = {}
            
            for pos, token in enumerate(doc_tokens):
                if token in query_terms:
                    positions.setdefault(token, []).append(pos)
            
            if len(positions) > 1:
                min_distances = []
                terms = list(positions.keys())
                
                for i in range(len(terms)):
                    for j in range(i + 1, len(terms)):
                        pos1 = positions[terms[i]]
                        pos2 = positions[terms[j]]
                        min_dist = min(abs(p1 - p2) for p1 in pos1 for p2 in pos2)
                        min_distances.append(min_dist)
                
                if min_distances:
                    scores[idx] = 1 / (1 + np.mean(min_distances))
        
        return scores

    def expand_query(self, query: str) -> str:
        """SRSWTI Query Expansion Module"""
        doc = self.nlp(query)
        expanded_terms = set([query])
            
        for token in doc:
            expanded_terms.add(token.lemma_)
                
            for synset in token._.wordnet.synsets():
                for lemma in synset.lemmas():
                    expanded_terms.add(lemma.name())
            
        logger.debug(f"SRSWTI Query Expansion: {' '.join(expanded_terms)}")
        return ' '.join(expanded_terms)
    def test_search_methods(self):
        """
        Test the search methods with sample documents and queries
        """
        # Sample documents
        documents = [
            "Machine learning is a powerful technology for data analysis",
            "Artificial intelligence helps solve complex problems",
            "Data science involves statistical modeling and machine learning techniques",
            "Neural networks are advanced computational models",
            "Python is a popular programming language for data science"
        ]
        
        # Test query expansion
        test_queries = [
            "machine learning",
            "data science",
            "artificial intelligence"
        ]
        
        print("\n=== Query Expansion Test ===")
        for query in test_queries:
            expanded_query = self.expand_query(query)
            print(f"Original Query: {query}")
            print(f"Expanded Query: {expanded_query}\n")
        
        # Test proximity-based scoring
        print("\n=== Proximity-Based Scoring Test ===")
        for query in test_queries:
            proximity_scores = self.calculate_proximity_scores(query, documents)
            print(f"Query: {query}")
            for doc, score in zip(documents, proximity_scores):
                print(f"  Document: {doc}")
                print(f"  Proximity Score: {score:.4f}\n")
        
        # Optional: Demonstrate full search workflow
        print("\n=== Full Search Workflow Test ===")
        query = "machine learning techniques"
        expanded_query = self.expand_query(query)
        proximity_scores = self.calculate_proximity_scores(expanded_query, documents)
        
        # Sort documents by proximity score
        ranked_docs = sorted(
            zip(documents, proximity_scores), 
            key=lambda x: x[1], 
            reverse=True
        )
        
        print(f"Search Query: {query}")
        print("Top Ranked Documents:")
        for doc, score in ranked_docs:
            print(f"  - {doc} (Score: {score:.4f})")


def main():
    # Initialize the search engine
    search_engine = SRSWTISearchEngine()
    
    # Sample documents
    documents = [
        "The quick brown fox jumps over the lazy dog",
        "Machine learning is transforming the technology landscape",
        "Python is a versatile programming language for data science",
        "Deep learning and neural networks are advancing AI capabilities",
        "Natural language processing helps computers understand human text",
        "The lazy dog sleeps while the quick fox watches"
    ]
    
    # Test different search queries
    queries = [
        "quick fox",
        "machine learning",
        "programming python",
    ]
    
    # Test different search approaches
    for query in queries:
        print(f"\n=== Testing search for: '{query}' ===\n")
        
        # Test hybrid search with default weights
        print("Hybrid Search Results:")
        results = search_engine.hybrid_search(query, documents)
        for idx, score in results:
            print(f"Score: {score:.4f} - {documents[idx]}")
        
        # Test with different weights
        custom_weights = {'bm25': 0.6, 'semantic': 0.3, 'proximity': 0.1}
        print("\nHybrid Search with Custom Weights:")
        results = search_engine.hybrid_search(query, documents, weights=custom_weights)
        for idx, score in results:
            print(f"Score: {score:.4f} - {documents[idx]}")

if __name__ == "__main__":
    main()