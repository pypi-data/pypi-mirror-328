
from wordllama import WordLlama
from typing import List, Tuple, Dict, Union, Optional
import json

class SrswtiClusterer:
    """Handles document clustering operations."""
    
    def __init__(self):
        self.model = WordLlama.load()
    
    def cluster_documents(self, documents: List[str], k: int = 3, 
                         max_iterations: int = 100, tolerance: float = 1e-4, 
                         n_init: int = 3) -> Tuple[List[int], float]:
        """
        Cluster documents using KMeans.
        okay so what im doing is pretty 
        Args:
            documents: Documents to cluster
            k: Number of clusters
            max_iterations: Maximum iterations for clustering
            tolerance: Convergence tolerance
            n_init: Number of initializations
            
        Returns:
            Tuple[List[int], float]: Cluster labels and inertia
        """
        return self.model.cluster(documents, k=k, max_iterations=max_iterations,
                                tolerance=tolerance, n_init=n_init)
