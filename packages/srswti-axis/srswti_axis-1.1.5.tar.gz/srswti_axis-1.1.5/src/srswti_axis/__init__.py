"""
SRSWTI AXIS: A Natural Language Processing Toolkit

This package provides various NLP utilities and tools for text processing,
classification, document analysis, search, sentiment analysis, summarization,
and translation.
"""

# Document Processing
from .document.deduplicator import SrswtiDeduplicator
from .document.base import DocumentProcessor
from .document.merger import SRSWTIPureFlow
from .document.clusterer import SrswtiClusterer
from .document.natural_chunking import (
    SRSWTIChunk,
    SRSWTIPhrase,
    SRSWTIChunkAnalyzer
)
from .document.ranker import SrswtiRanker
from .document.similarity import SrswtiSimilarity
from .document.splitter import SrswtiSplitter
from .document.topic_modeling import SRSWTIQuasar
from .document.merger import SRSWTIPureFlow

from .document.graph_merge import SRSWTIGraphFlow
from .document.jsd import SRSWTIDivergence

from .document.jsd2 import SRSWTIDivergenceV2

import nltk

nltk.download = lambda *args, **kwargs: None  # Disable automatic downloads


# Core Processing
from .core.base_processor import (
    SRSWTIBaseProcessor,
    SRSWTIProcessingError,
    SRSWTIConfigError,
    SRSWTIInputError,
    SRSWTIRuntimeError,
    ProcessingStatus,
    SRSWTIProcessingResult,
    SRSWTITextProcessor,
    SRSWTITokenizer,
    SRSWTIParser,
    SRSWTITagger
)
# from .core.nltk_processor import SRSWTINLTKProcessor
# from .core.spacy_processor import SRSWTISpacyProcessor
from .core.text_cleaner import SRSWTITextCleaner
from .core.toolkit import (
    SRSWTITextAnalyzer,
    SRSWTIEntityInfo,
    SRSWTISentenceInfo
)

# Search Engines
from .search_engines.bm25 import SRSWTISearchEngine 
from .search_engines.learn2rank import SRSWTIHilbertSearch
from .search_engines.ranker import SRSWTISearchRanker, SRSWTIUltimate

# Sentiment Analysis
from .sentiment.senti import SRSWTISentimentAnalyzer

# Classifier
from .classifier.misc import (
    SRSWTIZeroShot)

# LLM Integration
from .llm.main import SRSWTILanguageModel

# Scientific Processing
# from .scientific.scispacy_processor import SRSWTIScientificProcessor

# Summarization
from .summarize.main import (
    SRSWTISummarizer)
from .summarize.config import (
    SRSWTI_SUMMARIZATION_MODELS,
    SRSWTI_LONG_DOCUMENT_MODELS,
    LONG_DOCUMENT_CONFIGS,
    DEFAULT_CONFIG as SUMMARIZER_DEFAULT_CONFIG
)

# Translation
from .translation.misc import (
    SRSWTIMultilingualTranslator)

# def download_misc_helper_models():
#     """
#     Download miscellaneous helper models and resources for SRSWTI NLP toolkit.
    
#     This function handles downloading:
#     - spaCy 'en_core_web_sm' model
#     - NLTK resources
#     - Other potential language processing models
#     """
#     import subprocess
#     import sys
#     import logging

#     try:
#         # Download spaCy English model
#         subprocess.run(
#             [sys.executable, "-m", "spacy", "download", "en_core_web_sm"], 
#             check=True, 
#             capture_output=True
#         )
#         print("✅ ")

#         # Download NLTK resources
#         import nltk
#         nltk.download('punkt', quiet=True)
#         nltk.download('wordnet', quiet=True)
#         print("✅")

#     except subprocess.CalledProcessError as e:
#         logging.error(f"❌ Failed to download helper models: {e}")
#         raise
#     except Exception as e:
#         logging.error(f"❌ Unexpected error during model download: {e}")
#         raise

# Call download_misc_helper_models() when the package is first imported
# try:
#     download_misc_helper_models()
# except Exception as e:
#     print(f"Warning: Could not download helper models: {e}")

# Version Info
__version__ = "0.1.0"
__author__ = "TEAM SRSWTI"
__description__ = "SRSWTI NLP: A comprehensive toolkit for natural language processing tasks"
__license__ = "Proprietary"

# All exports
__all__ = [
    # Document Processing
    "DocumentProcessor",
    "SrswtiDeduplicator",
    "SRSWTIPureFlow",
    "SrswtiClusterer",
    "SRSWTIChunk",
    "SRSWTIPhrase",
    "SRSWTIChunkAnalyzer",
    "SrswtiRanker",
    "SrswtiSimilarity",
    "SrswtiSplitter",
    "SRSWTIQuasar",
    "SRSWTIDivergence",
    "SRSWTIDivergenceV2",
    "SRSWTIGraphFlow",
    
    # Core Processingxx
    "SRSWTIBaseProcessor",
    "SRSWTIProcessingError",
    "SRSWTIConfigError",
    "SRSWTIInputError",
    "SRSWTIRuntimeError",
    "ProcessingStatus",
    "SRSWTIProcessingResult",
    "SRSWTITextProcessor",
    "SRSWTITokenizer",
    "SRSWTIParser",
    "SRSWTITagger",
    "SRSWTINLTKProcessor",
    "SRSWTITextCleaner",
    "SRSWTITextAnalyzer",
    "SRSWTIEntityInfo",
    "SRSWTISentenceInfo",
    
    # Search Engines
    "SRSWTISearchEngine",
    "SRSWTIHilbertSearch",
    "SRSWTISearchRanker",
    "SRSWTIUltimate",
    
    # Sentiment Analysis
    "SRSWTISentimentAnalyzer",
    
    # Classifier
    "SRSWTIZeroShot",
    "SRSWTIClassifierConfig",
    
    # LLM
    "SRSWTILanguageModel",
    
    # Summarization
    "SRSWTISummarizer"
    
    # Translation
    "SRSWTITranslator",
    "TranslationConfig"
]