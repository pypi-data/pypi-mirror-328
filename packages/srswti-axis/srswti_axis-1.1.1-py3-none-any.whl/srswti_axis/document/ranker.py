from wordllama import WordLlama
from typing import List, Tuple, Dict, Union, Optional
import json


class SrswtiRanker:
    """Handles document ranking and filtering operations."""
    
    def __init__(self):
        self.model = WordLlama.load()
    
    def rank_documents(self, query: str, candidates: List[str], 
                      batch_size: int = 64) -> List[str]:
        """
        Rank documents based on similarity to query.
        
        Args:
            query: Search query
            candidates: List of documents to rank
            batch_size: Batch size for processing
            
        Returns:
            List[str]: Ranked documents
        """
        return self.model.rank(query, candidates, sort=True, batch_size=batch_size)
    
    def filter_documents(self, query: str, candidates: List[str], 
                        threshold: float = 0.3) -> List[str]:
        """
        Filter documents based on similarity threshold.
        
        Args:
            query: Reference query
            candidates: Documents to filter
            threshold: Minimum similarity threshold
            
        Returns:
            List[str]: Filtered documents
        """
        return self.model.filter(query, candidates, threshold=threshold)
    
    def get_top_k(self, query: str, candidates: List[str], k: int = 2) -> List[str]:
        """
        Retrieve top-K most similar documents.
        
        Args:
            query: Search query
            candidates: Candidate documents
            k: Number of documents to retrieve
            
        Returns:
            List[str]: Top K similar documents
        """
        return self.model.topk(query, candidates, k=k)
