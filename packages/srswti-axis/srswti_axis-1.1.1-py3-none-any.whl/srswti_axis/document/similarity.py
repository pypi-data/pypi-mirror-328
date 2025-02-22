from wordllama import WordLlama
from typing import List, Tuple, Dict, Union, Optional
import json


class SrswtiSimilarity:
    """Handles text similarity operations using WordLlama backend."""
    
    def __init__(self):
        self.model = WordLlama.load()
    
    def compute_similarity(self, text1: str, text2: str) -> float:
        """
        Calculate similarity between two texts.
        
        Args:
            text1: First text string
            text2: Second text string
            
        Returns:
            float: Similarity score between 0 and 1
        """
        return float(self.model.similarity(text1, text2))