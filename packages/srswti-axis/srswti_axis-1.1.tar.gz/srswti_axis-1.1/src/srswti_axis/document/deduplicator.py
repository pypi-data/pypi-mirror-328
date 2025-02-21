from wordllama import WordLlama
from typing import List, Tuple, Dict, Union, Optional
import json

class SrswtiDeduplicator:
    """Handles document deduplication."""
    
    def __init__(self):
        self.model = WordLlama.load()
    
    def deduplicate(self, documents: List[str], threshold: float = 0.5, 
                   return_indices: bool = False) -> Union[List[str], Tuple[List[str], List[int]]]:
        """
        Remove near-duplicate documents.
        
        Args:
            documents: List of documents to deduplicate
            threshold: Similarity threshold for considering duplicates
            return_indices: Whether to return indices of unique documents
            
        Returns:
            Union[List[str], Tuple[List[str], List[int]]]: Deduplicated documents
        """
        return self.model.deduplicate(documents, threshold=threshold, return_indices=return_indices)
