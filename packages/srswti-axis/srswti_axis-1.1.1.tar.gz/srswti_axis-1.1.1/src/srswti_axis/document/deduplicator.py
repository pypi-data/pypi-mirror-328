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
def main():
    """
    Example usage of SrswtiDeduplicator.
    
    Demonstrates deduplication of a list of documents with near-duplicates.
    """
    # Prepare a diverse set of documents with some duplicates and near-duplicates
    documents = [
        "Apple Inc. announced a groundbreaking AI technology that could revolutionize machine learning.",
        "Apple Inc. revealed an innovative AI solution transforming machine learning paradigms.",  # Near-duplicate
        "Climate change is driving significant innovations in renewable energy solutions worldwide.",
        "Renewable energy solutions are critical in addressing global climate change challenges.",  # Similar
        "The latest quantum computing breakthrough promises to transform cryptography and scientific research.",
        "Quantum computing is set to revolutionize cryptographic methods and scientific investigations.",  # Similar
    ]

    # Create a deduplicator instance
    deduplicator = SrswtiDeduplicator()

    # Perform deduplication with default threshold
    unique_docs = deduplicator.deduplicate(documents, threshold=0.5)
    
    # Print the unique documents
    print("Unique Documents:", unique_docs)

if __name__ == "__main__":
    main()
