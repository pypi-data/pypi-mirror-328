# base_processor.py

import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List, Optional, Union, Tuple
from pathlib import Path
import json
import traceback, time, datetime

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

class SRSWTIProcessingError(Exception):
    """Base exception class for all SRSWTI processing errors."""
    def __init__(self, message: str, error_code: str, details: Optional[Dict] = None):
        self.error_code = error_code
        self.details = details or {}
        super().__init__(f"{error_code}: {message}")

class SRSWTIConfigError(SRSWTIProcessingError):
    """Configuration related errors."""
    pass

class SRSWTIInputError(SRSWTIProcessingError):
    """Input validation errors."""
    pass

class SRSWTIRuntimeError(SRSWTIProcessingError):
    """Runtime processing errors."""
    pass

class ProcessingStatus(Enum):
    SUCCESS = "success"
    PARTIAL_SUCCESS = "partial_success"
    FAILURE = "failure"

@dataclass
class SRSWTIProcessingResult:
    """Standardized container for processing results."""
    content: Any
    status: ProcessingStatus
    metadata: Dict[str, Any]
    errors: List[Dict[str, Any]]
    warnings: List[Dict[str, Any]]

    def to_dict(self) -> Dict[str, Any]:
        """Convert result to dictionary format."""
        return {
            "content": self.content,
            "status": self.status.value,
            "metadata": self.metadata,
            "errors": self.errors,
            "warnings": self.warnings
        }

    def to_json(self) -> str:
        """Convert result to JSON string."""
        return json.dumps(self.to_dict())

class SRSWTIBaseProcessor(ABC):
    """Abstract base class for all SRSWTI NLP processors."""
    
    def __init__(
        self,
        config_path: Optional[Union[str, Path]] = None,
        config: Optional[Dict[str, Any]] = None,
        logger: Optional[logging.Logger] = None
    ):
        """
        Initialize the processor.
        
        Args:
            config_path: Path to configuration file
            config: Configuration dictionary
            logger: Custom logger instance
        """
        self.logger = logger or logging.getLogger(self.__class__.__name__)
        self.config = self._load_config(config_path) if config_path else config or {}
        self._initialize()

    def _load_config(self, config_path: Union[str, Path]) -> Dict[str, Any]:
        """Load configuration from file."""
        try:
            with open(config_path) as f:
                config = json.load(f)
            self.logger.info(f"Configuration loaded from {config_path}")
            return config
        except Exception as e:
            error_msg = f"Failed to load configuration from {config_path}"
            self.logger.error(f"{error_msg}: {str(e)}")
            raise SRSWTIConfigError(error_msg, "CONFIG_LOAD_ERROR", 
                                  {"path": str(config_path), "error": str(e)})

    @abstractmethod
    def _initialize(self) -> None:
        """Initialize processor-specific resources."""
        pass

    def validate_input(self, text: Union[str, List[str]]) -> Tuple[bool, Optional[str]]:
        """
        Validate input text before processing.
        
        Args:
            text: Input text or list of texts
            
        Returns:
            Tuple of (is_valid, error_message)
        """
        if text is None:
            return False, "Input text cannot be None"
            
        if isinstance(text, str):
            if not text.strip():
                return False, "Input text cannot be empty"
        elif isinstance(text, list):
            if not text:
                return False, "Input text list cannot be empty"
            if not all(isinstance(t, str) for t in text):
                return False, "All elements must be strings"
            if not all(t.strip() for t in text):
                return False, "All texts must be non-empty"
        else:
            return False, f"Input must be string or list of strings, got {type(text)}"
            
        return True, None

    def process_with_error_handling(
        self,
        func: callable,
        *args,
        **kwargs
    ) -> SRSWTIProcessingResult:
        """
        Wrapper for processing functions with standardized error handling.
        
        Args:
            func: Processing function to execute
            *args: Positional arguments for func
            **kwargs: Keyword arguments for func
            
        Returns:
            SRSWTIProcessingResult
        """
        errors = []
        warnings = []
        
        try:
            # Validate input if present in kwargs
            if 'text' in kwargs:
                is_valid, error_msg = self.validate_input(kwargs['text'])
                if not is_valid:
                    # Raise the input error instead of returning a failure result
                    raise SRSWTIInputError(error_msg, "INPUT_VALIDATION_ERROR")

            # If no text in kwargs, try to validate the first positional argument
            elif args:
                is_valid, error_msg = self.validate_input(args[0])
                if not is_valid:
                    # Raise the input error instead of returning a failure result
                    raise SRSWTIInputError(error_msg, "INPUT_VALIDATION_ERROR")

            # Execute processing function
            start_time = time.time()
            result = func(*args, **kwargs)
            processing_time = time.time() - start_time

            # Create successful result
            return SRSWTIProcessingResult(
                content=result,
                status=ProcessingStatus.SUCCESS,
                metadata={
                    "processor": self.__class__.__name__,
                    "processing_time": processing_time,
                    "timestamp": datetime.datetime.now().isoformat()
                },
                errors=errors,
                warnings=warnings
            )

        except SRSWTIProcessingError:
            # Re-raise SRSWTIProcessingError to propagate input validation errors
            raise

        except Exception as e:
            self.logger.error(f"Unexpected error: {str(e)}")
            errors.append({
                "code": "UNEXPECTED_ERROR",
                "message": str(e),
                "details": {"type": type(e).__name__},
                "traceback": traceback.format_exc()
            })

            # Return failure result if we get here
            return SRSWTIProcessingResult(
                content=None,
                status=ProcessingStatus.FAILURE,
                metadata={
                    "processor": self.__class__.__name__,
                    "timestamp": datetime.datetime.now().isoformat()
                },
                errors=errors,
                warnings=warnings
            )

class SRSWTITextProcessor(SRSWTIBaseProcessor):
    """Base class for text processing operations."""
    
    @abstractmethod
    def process_text(
        self,
        text: Union[str, List[str]],
        **kwargs
    ) -> SRSWTIProcessingResult:
        """
        Process input text.
        
        Args:
            text: Input text or list of texts
            **kwargs: Additional processing parameters
            
        Returns:
            Processing result
        """
        pass

class SRSWTITokenizer(SRSWTITextProcessor):
    """Base class for tokenization operations."""
    
    @abstractmethod
    def tokenize(
        self,
        text: str,
        **kwargs
    ) -> SRSWTIProcessingResult:
        """
        Tokenize input text.
        
        Args:
            text: Input text
            **kwargs: Additional tokenization parameters
            
        Returns:
            Tokenization result
        """
        pass
    
    @abstractmethod
    def detokenize(
        self,
        tokens: List[str],
        **kwargs
    ) -> SRSWTIProcessingResult:
        """
        Combine tokens back into text.
        
        Args:
            tokens: List of tokens
            **kwargs: Additional detokenization parameters
            
        Returns:
            Detokenization result
        """
        pass

class SRSWTIParser(SRSWTITextProcessor):
    """Base class for parsing operations."""
    
    @abstractmethod
    def parse(
        self,
        text: str,
        **kwargs
    ) -> SRSWTIProcessingResult:
        """
        Parse input text.
        
        Args:
            text: Input text
            **kwargs: Additional parsing parameters
            
        Returns:
            Parsing result
        """
        pass

class SRSWTITagger(SRSWTITextProcessor):
    """Base class for tagging operations."""
    
    @abstractmethod
    def tag(
        self,
        text: str,
        **kwargs
    ) -> SRSWTIProcessingResult:
        """
        Tag input text.
        
        Args:
            text: Input text
            **kwargs: Additional tagging parameters
            
        Returns:
            Tagging result
        """
        pass