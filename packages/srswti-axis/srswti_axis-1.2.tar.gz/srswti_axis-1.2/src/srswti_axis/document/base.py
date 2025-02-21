from abc import ABC, abstractmethod
from typing import List, Dict, Union, Tuple, Optional

class DocumentProcessor(ABC):
    """Base class for document processing operations."""
    @abstractmethod
    def process(self):
        pass

