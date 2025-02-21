# main.py

import torch
from transformers import (
    AutoModelForSeq2SeqLM, 
    AutoTokenizer, 
    pipeline,
    logging as transformers_logging
)
from typing import List, Dict, Union, Optional
import logging
from dataclasses import dataclass
from datetime import datetime
import gc
import os
import sys
from pathlib import Path
import json
import warnings
import nltk

nltk.download = lambda *args, **kwargs: None  # Disable automatic downloads
# Suppress warnings
warnings.filterwarnings('ignore')
transformers_logging.set_verbosity_error()

# Constants imports
from srswti_axis.summarize.config  import (
    SRSWTI_SUMMARIZATION_MODELS,
    SRSWTI_LONG_DOCUMENT_MODELS,
    LONG_DOCUMENT_CONFIGS
)

class SRSWTILogger:
    @staticmethod
    def setup(level=logging.INFO, log_file=None):
        # Suppress NLTK download logs
        logging.getLogger('nltk_data').setLevel(logging.ERROR)
        
        logger = logging.getLogger("SRSWTI-Summarizer")
        logger.setLevel(level)
        
        formatter = logging.Formatter(
            '%(asctime)s [%(levelname)s] SRSWTI-Summarizer: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        
        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        
        return logger

@dataclass
class SRSWTISummaryConfig:
    """Configuration for SRSWTI Summarizer"""
    model_type: str = "lightweight"  # lightweight, medium, large, xlarge, specialized
    model_name: str = "srswti_olympus"  # specific model within type
    device: str = None
    use_long_model: bool = False
    long_model_type: str = None
    document_type: str = None  # for long documents: book_summary, technical_doc, etc.
    log_file: str = "./srswti_summarizer.log"
    
    def __post_init__(self):
        if self.device is None:
            self.device = "cuda" if torch.cuda.is_available() else "cpu"

class SRSWTISummarizer:
    """SRSWTI Advanced Summarization System"""
    
    def __init__(self, config: SRSWTISummaryConfig):
        self.config = config
        self.logger = SRSWTILogger.setup(log_file=config.log_file)
        self._setup_environment()
        self._load_model()
        

    def _setup_environment(self):
        """Setup environment"""
        self.logger.info(f"Initializing SRSWTI Summarizer on {self.config.device.upper()}")

    def _get_model_config(self):
        """Get model configuration based on type"""
        if not self.config.use_long_model:
            # Always show SRSWTI Olympus branding even though using distilbart underneath
            model_name = self.config.model_name
            model_group = SRSWTI_SUMMARIZATION_MODELS[self.config.model_type]
            return model_group["distilbart"]  # Always use distilbart under the hood
        else:
            return SRSWTI_LONG_DOCUMENT_MODELS["long_document"][self.config.long_model_type]


    def _load_model(self):
        """Load the appropriate model based on configuration"""
        try:
            model_config = self._get_model_config()
            branded_name = "SRSWTI-OLYMPUS" if self.config.model_name == "srswti_olympus" else model_config['name']
            self.logger.info(f"Loading model: {branded_name}")  
            
            self.summarizer = pipeline(
                "summarization",
                model=model_config['name'],  # Still use actual model name for loading
                device=0 if self.config.device == "cuda" else -1
            )
            
            self.model_params = model_config['params']
            
            self.logger.info(f"{branded_name} loaded successfully. Size: {model_config['size']}")
            
        except Exception as e:
            self.logger.error(f"Error loading model: {str(e)}")
            raise

    def _preprocess_text(self, text: str) -> str:
        """Preprocess text for summarization"""
        return ' '.join(text.split())

    def _chunk_long_document(self, text: str) -> List[str]:
        """Split long documents into overlapping chunks"""
        if not self.config.document_type:
            return [text]
            
        config = LONG_DOCUMENT_CONFIGS[self.config.document_type]
        chunk_size = config['chunk_size']
        overlap = config['overlap']
        
        words = text.split()
        chunks = []
        start = 0
        
        while start < len(words):
            end = start + chunk_size
            chunk = ' '.join(words[start:end])
            chunks.append(chunk)
            start += chunk_size - overlap
            
        return chunks

    def _merge_summaries(self, summaries: List[str]) -> str:
        """Merge multiple chunk summaries into one"""
        if len(summaries) == 1:
            return summaries[0]
            
        combined = ' '.join(summaries)
        final_summary = self.summarizer(
            combined,
            max_length=self.model_params['max_length'],
            min_length=self.model_params['min_length'],
            length_penalty=self.model_params['length_penalty']
        )[0]['summary_text']
        
        return final_summary

    def summarize(
        self,
        text: Union[str, List[str]],
        custom_params: Optional[Dict] = None
    ) -> Dict:
        """
        Generate summary for text or list of texts
        """
        start_time = datetime.now()
        
        try:
            texts = [text] if isinstance(text, str) else text
            all_summaries = []
            
            params = custom_params or self.model_params
            
            for text in texts:
                processed_text = self._preprocess_text(text)
                chunks = self._chunk_long_document(processed_text)
                
                chunk_summaries = []
                for i, chunk in enumerate(chunks):
                    self.logger.debug(f"Processing chunk {i+1}/{len(chunks)}")
                    
                    summary = self.summarizer(
                        chunk,
                        **params
                    )[0]['summary_text']
                    
                    chunk_summaries.append(summary)
                    
                    if self.config.device == "cuda":
                        torch.cuda.empty_cache()
                    gc.collect()
                
                final_summary = self._merge_summaries(chunk_summaries)
                all_summaries.append(final_summary)
            
            processing_time = (datetime.now() - start_time).total_seconds()
            
            return {
                'summaries': all_summaries,
                'metadata': {
                    'model_type': self.config.model_type,
                    'model_name': 'SRSWTI-OLYMPUS',  # Show SRSWTI branding
                    'num_texts': len(texts),
                    'processing_time': round(processing_time, 2),
                    'device': self.config.device.upper(),
                    'document_type': self.config.document_type
                }
            }
            
        except Exception as e:
            self.logger.error(f"Summarization error: {str(e)}")
            raise

def main():
    try:
        # Example 1: Quick summarization with lightweight model
        config_light = SRSWTISummaryConfig(
            model_type="lightweight",
            model_name="srswti_olympus"
        )
        summarizer_light = SRSWTISummarizer(config_light)
        
        text = """
        Dark matter represents one of the most profound mysteries in modern astrophysics, constituting approximately 27% of the universe's total mass-energy content yet remaining fundamentally undetectable through direct observation.
        Sophisticated astronomical techniques like gravitational lensing and galactic rotation studies provide compelling evidence for its existence, challenging our fundamental understanding of cosmic structure and fundamental physics.
        
        Kepler-12b, an exoplanet located approximately 1,200 light-years from Earth, exemplifies the extraordinary diversity of planetary systems beyond our solar neighborhood, presenting unique characteristics that intrigue planetary scientists and astronomers.
        This gas giant, discovered through the groundbreaking Kepler space telescope mission, orbits its parent star with remarkable orbital dynamics that challenge traditional planetary formation models.
        
        The intersection of dark matter research and exoplanetary studies reveals profound connections between cosmic-scale phenomena and localized planetary environments, suggesting complex interactions between fundamental gravitational forces and stellar system architectures.
        
        Advanced computational models and next-generation telescopes like the James Webb Space Telescope are progressively unraveling the intricate relationships between dark matter distributions, stellar evolution, and planetary system formation, pushing the boundaries of our astronomical comprehension.
        
        Theoretical physicists and astronomers continue to develop increasingly sophisticated methodologies to probe the enigmatic nature of dark matter, utilizing cutting-edge technologies and interdisciplinary research approaches to decode the universe's most fundamental mysteries.
        """
        
        result = summarizer_light.summarize(text)
        print("\nLightweight Model Summary:")
        print(result['summaries'][0])
        print("\nMetadata:", result['metadata'])

        # Clean up resources
        del summarizer_light.summarizer
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        gc.collect()
        
        print("\n✅ Summarization completed successfully!")

    except Exception as e:
        logging.error(f"Error in main: {str(e)}")
        sys.exit(1)
    finally:
        # Force exit to clean up any hanging threads
        os._exit(0)

if __name__ == "__main__":
    main()