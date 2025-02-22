from typing import List, Dict, Tuple, Optional
import numpy as np
from scipy.sparse import csr_matrix
import networkx as nx
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import spacy

class SRSWTISearchRanker:
    """
    Advanced document ranking using PageRank and semantic similarity
    """
    def __init__(self, 
                 embedding_model: str = 'srswti-neural-embedder-v1',
                 use_pagerank: bool = True):
        # Map SRSWTI model alias to the actual model
        model_mapping = {
            'srswti-neural-embedder-v1': 'all-mpnet-base-v2'
        }
        actual_model = model_mapping.get(embedding_model, embedding_model)
        self.embedder = SentenceTransformer(actual_model)
        self.nlp = spacy.load('en_core_web_sm')
        self.use_pagerank = use_pagerank
        self.doc_embeddings = None
        self.document_graph = None
        self.pagerank_scores = None
        
    def build_document_graph(self, 
                       documents: List[str],
                        threshold: float = 0.5) -> nx.DiGraph:
        """
        Build document similarity graph for PageRank
        """
        # Get embeddings for all documents
        self.doc_embeddings = self.embedder.encode(documents)
        
        # Calculate similarity matrix
        similarity_matrix = cosine_similarity(self.doc_embeddings)
        
        # Create graph
        G = nx.DiGraph()
        
        # Add nodes first (important for isolated nodes)
        for i in range(len(documents)):
            G.add_node(i)
        
        # Add edges based on similarity threshold
        for i in range(len(documents)):
            for j in range(len(documents)):
                if i != j and similarity_matrix[i][j] > threshold:
                    G.add_edge(i, j, weight=similarity_matrix[i][j])
        
        self.document_graph = G
        
        # Ensure there's at least one edge by connecting to nearest neighbor if graph is empty
        if G.number_of_edges() == 0:
            for i in range(len(documents)):
                if i < len(documents) - 1:
                    G.add_edge(i, i + 1, weight=0.1)
        
        # Calculate PageRank scores, make sure to have it staged
        self.pagerank_scores = nx.pagerank(G, alpha=0.85)
        
        return G
    
    def rank_documents(self, 
                      query: str, 
                      documents: List[str],
                      combine_method: str = 'weighted_sum',
                      alpha: float = 0.3) -> List[Tuple[int, float]]:
        """
        Rank documents using combination of semantic similarity and PageRank
        
        Args:
            query: Search query
            documents: List of documents
            combine_method: How to combine PageRank and similarity ('weighted_sum' or 'multiplication')
            alpha: Weight for PageRank score (1-alpha for similarity score)
            
        Returns:
            List of (document_idx, score) sorted by relevance
        """
        # Get query embedding
        if self.doc_embeddings is None or self.pagerank_scores is None:
            self.build_document_graph(documents)
        query_embedding = self.embedder.encode([query])[0]
        
        # Calculate semantic similarities
        similarities = cosine_similarity([query_embedding], self.doc_embeddings)[0]
        
        # Combine scores
        if combine_method == 'weighted_sum':
            final_scores = alpha * np.array(list(self.pagerank_scores.values())) + \
                         (1 - alpha) * similarities
        else:  # multiplication
            final_scores = np.array(list(self.pagerank_scores.values())) * similarities
        
        # Sort and return indices
        ranked_indices = np.argsort(-final_scores)
        return [(idx, final_scores[idx]) for idx in ranked_indices]
    
    def get_document_clusters(self) -> Dict[int, List[int]]:
        """
        Get document clusters based on graph structure
        """
        return {
            idx: list(component)
            for idx, component in enumerate(nx.connected_components(self.document_graph.to_undirected()))
        }

class SRSWTIUltimate:
    """
    Complete search engine with multiple ranking methods
    """
    def __init__(self):
        self.ranker = SRSWTISearchRanker()
        self.documents = []
        self.doc_embeddings = None
        
    def index_documents(self, documents: List[str]):
        """
        Index documents and build necessary data structures
        """
        self.documents = documents
        self.ranker.build_document_graph(documents)
        
    def search(self, 
              query: str,
              n_results: int = 5,
              ranking_method: str = 'combined') -> List[Dict]:
        """
        Search documents with specified ranking method
        """
        # Get ranked documents
        ranked_docs = self.ranker.rank_documents(
            query,
            self.documents,
            combine_method='weighted_sum' if ranking_method == 'combined' else 'multiplication'
        )
        
        # Prepare results
        results = []
        for doc_idx, score in ranked_docs[:n_results]:
            results.append({
                'document': self.documents[doc_idx],
                'score': score,
                'pagerank': self.ranker.pagerank_scores[doc_idx],
                'cluster': self._get_document_cluster(doc_idx)
            })
        
        return results
    
    def _get_document_cluster(self, doc_idx: int) -> int:
        """Get cluster ID for document"""
        clusters = self.ranker.get_document_clusters()
        for cluster_id, docs in clusters.items():
            if doc_idx in docs:
                return cluster_id
        return -1

# Example Usage
def main():
    # Sample documents
    documents = [
        "Machine learning is a subset of artificial intelligence.",
        "Deep learning models require significant computational resources.",
        "Natural language processing helps computers understand human language.",
        "Neural networks are inspired by biological neurons.",
        "Artificial intelligence is revolutionizing technology.",
        "Electric cars are transforming the automotive industry.",
        "Tesla's advanced battery technology improves vehicle range.",
        "Autonomous driving systems use complex machine learning algorithms.",
        "Automotive engineering focuses on efficiency and performance.",
        "Modern cars integrate sophisticated computer systems.",
        "Bikinis represent evolving fashion trends in swimwear design.",
        "Beach fashion highlights diverse styles of swimwear."
    ]
    
    try:
        # Initialize search engine
        search_engine = SRSWTIUltimate()
        
        # Index documents
        search_engine.index_documents(documents)
        
        # Perform search
        query = "kanye west is an american rapper and a machine learnig professor at an electric company"
        results = search_engine.search(query, n_results=3)
        
        # Print results
        print(f"\nSearch Results for: {query}\n")
        for i, result in enumerate(results, 1):
            print(f"Result {i}:")
            print(f"Document: {result['document']}")
            print(f"Score: {result['score']:.3f}")
            print(f"PageRank: {result['pagerank']:.3f}")
            print(f"Cluster: {result['cluster']}")
            print()
    finally:
        # Clear any references to large objects
        if 'search_engine' in locals():
            search_engine.ranker.embedder = None
            search_engine.ranker.nlp = None

if __name__ == "__main__":
    main()