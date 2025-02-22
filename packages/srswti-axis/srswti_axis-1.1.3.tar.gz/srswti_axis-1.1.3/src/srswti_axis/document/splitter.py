from wordllama import WordLlama
from typing import List, Tuple, Dict, Union, Optional
import json

class SrswtiSplitter:
    """Handles text splitting operations."""
    
    def __init__(self):
        self.model = WordLlama.load()
    
    def split_text(self, text: str, target_size: int = 1536) -> List[str]:
        """
        Split text into semantic chunks.
        
        Args:
            text: Text to split
            target_size: Target size for chunks
            
        Returns:
            List[str]: List of text chunks
        """
        return self.model.split(text, target_size=target_size)
    
    def get_chunk_info(self, chunks: List[str]) -> Dict[str, Union[List[int], List[str]]]:
        """
        Get information about text chunks.
        
        Args:
            chunks: List of text chunks
            
        Returns:
            Dict: Dictionary containing chunk lengths and content
        """
        return {
            "chunk_lengths": list(map(len, chunks)),
            "chunks": chunks
        }