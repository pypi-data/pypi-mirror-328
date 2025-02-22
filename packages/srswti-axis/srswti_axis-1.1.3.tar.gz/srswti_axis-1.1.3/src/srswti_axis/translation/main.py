from transformers import MarianMTModel, MarianTokenizer
import torch
from typing import List, Dict, Union
import logging
from dataclasses import dataclass
from datetime import datetime
import sys
import gc
from tqdm import tqdm
import psutil
import os
import traceback

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] SRSWTI-Translator: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

@dataclass
class TranslationConfig:
    """Configuration for SRSWTI Translator"""
    device: str = None
    batch_size: int = 8
    max_length: int = 512
    beam_size: int = 4
    num_hypotheses: int = 1
    cache_dir: str = "./translation_cache"
    low_cpu_mem_usage: bool = True
    force_cleanup: bool = True
    log_level: str = "INFO"

class SRSWTITrans:
    """SRSWTI Multi-Language Translation System"""
    
    LANGUAGE_CODES = {
        'English': 'en', 'Spanish': 'es', 'French': 'fr',
        'German': 'de', 'Italian': 'it', 'Portuguese': 'pt',
        'Russian': 'ru', 'Chinese': 'zh', 'Japanese': 'ja',
        'Korean': 'ko', 'Arabic': 'ar', 'Hindi': 'hi',
        'Dutch': 'nl', 'Polish': 'pl', 'Turkish': 'tr'
    }

    def __init__(self, config: TranslationConfig = None):
        self.config = config or TranslationConfig()
        self.logger = logging.getLogger("SRSWTI-Translator")
        self.logger.setLevel(self.config.log_level)
        self._setup_system()
        self.models = {}
        self.tokenizers = {}

    def _setup_system(self):
        """Setup system and check resources"""
        try:
            self.logger.info("Initializing SRSWTI Translation System...")
            
            # Check system resources
            mem = psutil.virtual_memory()
            self.logger.info(f"Available System Memory: {mem.available / (1024**3):.2f}GB")
            
            # Set device with detailed logging
            if self.config.device is None:
                cuda_available = torch.cuda.is_available()
                self.device = "cuda" if cuda_available else "cpu"
                if cuda_available:
                    self.logger.info(f"CUDA Device: {torch.cuda.get_device_name(0)}")
                    self.logger.info(f"CUDA Memory: {torch.cuda.get_device_properties(0).total_memory / (1024**3):.2f}GB")
            else:
                self.device = self.config.device
                
            self.logger.info(f"SRSWTI Translator will use {self.device.upper()} for processing")
            
            # Create cache directory if needed
            if self.config.cache_dir and not os.path.exists(self.config.cache_dir):
                os.makedirs(self.config.cache_dir)
                
        except Exception as e:
            self.logger.error(f"System setup failed: {str(e)}")
            self.logger.error(traceback.format_exc())
            raise

    def _get_model_name(self, source_lang: str, target_lang: str) -> str:
        """Get the appropriate Helsinki-NLP model name for language pair"""
        source_code = self.LANGUAGE_CODES.get(source_lang, source_lang.lower())
        target_code = self.LANGUAGE_CODES.get(target_lang, target_lang.lower())
        return f"Helsinki-NLP/opus-mt-{source_code}-{target_code}"

    def _load_model(self, source_lang: str, target_lang: str):
        """Load translation model with progress tracking"""
        model_name = self._get_model_name(source_lang, target_lang)
        model_key = f"{source_lang}-{target_lang}"
        
        try:
            if model_key not in self.models:
                self.logger.info(f"Loading translation model: {model_name}")
                
                # Progress bar for model loading
                with tqdm(total=2, desc=f"Loading {source_lang}->{target_lang} Model") as pbar:
                    # Load tokenizer
                    self.tokenizers[model_key] = MarianTokenizer.from_pretrained(
                        model_name,
                        cache_dir=self.config.cache_dir
                    )
                    pbar.update(1)
                    
                    # Load model with memory optimization
                    model_kwargs = {
                        "low_cpu_mem_usage": self.config.low_cpu_mem_usage,
                        "cache_dir": self.config.cache_dir
                    }
                    
                    self.models[model_key] = MarianMTModel.from_pretrained(
                        model_name,
                        **model_kwargs
                    )
                    
                    if self.device == "cuda":
                        self.models[model_key] = self.models[model_key].to("cuda")
                    pbar.update(1)
                
                self.logger.info(f"Model loaded successfully: {model_name}")
                
                if self.config.force_cleanup:
                    gc.collect()
                    if self.device == "cuda":
                        torch.cuda.empty_cache()
                        
        except Exception as e:
            self.logger.error(f"Error loading model {model_name}: {str(e)}")
            self.logger.error(traceback.format_exc())
            raise

    def translate(
        self,
        texts: Union[str, List[str]],
        source_lang: str,
        target_lang: str
    ) -> Dict:
        """Translate text(s) with progress tracking and memory management"""
        start_time = datetime.now()
        
        try:
            # Convert single text to list
            if isinstance(texts, str):
                texts = [texts]
            
            # Load model if needed
            model_key = f"{source_lang}-{target_lang}"
            if model_key not in self.models:
                self._load_model(source_lang, target_lang)
            
            model = self.models[model_key]
            tokenizer = self.tokenizers[model_key]
            
            translations = []
            # Process in batches with progress bar
            with tqdm(total=len(texts), desc="Translating") as pbar:
                for i in range(0, len(texts), self.config.batch_size):
                    batch = texts[i:i + self.config.batch_size]
                    
                    # Tokenize
                    encoded = tokenizer(
                        batch,
                        return_tensors="pt",
                        padding=True,
                        truncation=True,
                        max_length=self.config.max_length
                    )
                    
                    if self.device == "cuda":
                        encoded = encoded.to("cuda")
                    
                    # Translate
                    translated = model.generate(
                        **encoded,
                        num_beams=self.config.beam_size,
                        num_return_sequences=self.config.num_hypotheses,
                        max_length=self.config.max_length
                    )
                    
                    # Decode
                    batch_translations = tokenizer.batch_decode(
                        translated,
                        skip_special_tokens=True
                    )
                    
                    translations.extend(batch_translations)
                    pbar.update(len(batch))
                    
                    # Clean up memory after each batch
                    if self.config.force_cleanup:
                        del encoded, translated
                        if self.device == "cuda":
                            torch.cuda.empty_cache()
                        gc.collect()
            
            processing_time = (datetime.now() - start_time).total_seconds()
            
            return {
                'translations': translations,
                'metadata': {
                    'source_language': source_lang,
                    'target_language': target_lang,
                    'num_texts': len(texts),
                    'processing_time': round(processing_time, 2),
                    'device': self.device.upper(),
                    'model': self._get_model_name(source_lang, target_lang),
                    'batch_size': self.config.batch_size,
                    'max_length': self.config.max_length
                }
            }
            
        except Exception as e:
            self.logger.error(f"Translation error: {str(e)}")
            self.logger.error(traceback.format_exc())
            raise

def print_translation_results(results: Dict):
    """Helper function to print translation results"""
    try:
        print("\nSRSWTI Translation Results")
        print("=" * 50)
        
        meta = results['metadata']
        print(f"\nTranslation Details:")
        print(f"• Source Language: {meta['source_language']}")
        print(f"• Target Language: {meta['target_language']}")
        print(f"• Number of Texts: {meta['num_texts']}")
        
        print("\nTranslations:")
        for i, translation in enumerate(results['translations'], 1):
            print(f"\n{i}. {translation}")
        
        print("\nSystem Information")
        print("=" * 50)
        print(f"• Model:           {meta['model']}")
        print(f"• Device:          {meta['device']}")
        print(f"• Processing Time: {meta['processing_time']} seconds")
        print(f"• Batch Size:      {meta['batch_size']}")
        print(f"• Max Length:      {meta['max_length']}")
        
    except Exception as e:
        print(f"Error printing results: {str(e)}")
        traceback.print_exc()
def main():
    try:
        # Initialize with optimized configuration
        config = TranslationConfig(
            device="cpu",  # Explicitly set device
            batch_size=4,  # Smaller batch size for better memory management
            max_length=512,  # Increased max length for longer texts
            low_cpu_mem_usage=True,
            force_cleanup=True,
            cache_dir="./translation_cache"
        )
        
        print("\nInitializing SRSWTI Translator...")
        translator = SRSWTITrans(config)
        
        # Example translations with more complex and longer texts
        translation_tasks = [
            {
                "texts": [
                    "Hello, how are you? I hope you're having a wonderful day filled with joy and happiness.",
                    "The weather is absolutely stunning today, with clear blue skies and a gentle breeze that makes everything feel perfect.",
                    "In the bustling city, people from all walks of life come together, creating a vibrant tapestry of human experience and cultural diversity."
                ],
                "source": "English",
                "target": "Spanish"
            },
            {
                "texts": [
                    "This is an extremely complex technical document detailing the intricate mechanisms of advanced machine learning algorithms and their potential applications in various scientific domains.",
                    "Please translate this comprehensive research paper with the utmost care and precision, ensuring that the technical nuances and scientific terminology are accurately preserved.",
                    "The intersection of artificial intelligence, quantum computing, and neuromorphic engineering represents a groundbreaking frontier in computational science and technological innovation."
                ],
                "source": "English",
                "target": "German"
            },
            {
                "texts": [
                    "Imagine a world where technology and human creativity seamlessly blend to solve the most pressing global challenges, from climate change to healthcare accessibility.",
                    "The future of innovation lies not in competition, but in collaborative efforts that transcend geographical, cultural, and disciplinary boundaries.",
                    "Every breakthrough begins with a simple idea, nurtured by curiosity, powered by persistence, and realized through collective human potential."
                ],
                "source": "English",
                "target": "French"
            }
        ]
        
        # Process each translation task
        for task in tqdm(translation_tasks, desc="Processing Translation Tasks"):
            print(f"\nTranslating from {task['source']} to {task['target']}")
            
            result = translator.translate(
                texts=task['texts'],
                source_lang=task['source'],
                target_lang=task['target']
            )
            
            print_translation_results(result)
            
            # Force cleanup between tasks
            if config.force_cleanup:
                gc.collect()
                if torch.cuda.is_available():
                    torch.cuda.empty_cache()
                    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        traceback.print_exc()

if __name__ == "__main__":
    main()