import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer, logging as transformers_logging
from typing import List, Dict, Union
import logging
from dataclasses import dataclass
from datetime import datetime
import sys
import traceback
import numpy as np
import gc
from tqdm import tqdm
import psutil
import os

# Constants
INTERNAL_MODEL = "facebook/bart-large-mnli"
SRSWTI_MODEL_NAME = "SRSWTI-ZeroShot-Classifier-v1" 
SRSWTI_VERSION = "1.0.0"

# Configure logging with more detail
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] SRSWTI-ZeroShot: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Suppress transformer warnings
transformers_logging.set_verbosity_error()

@dataclass
class SRSWTIConfig:
    """Configuration for SRSWTI Zero Shot Classifier"""
    device: str = None
    model_name: str = SRSWTI_MODEL_NAME
    internal_model: str = INTERNAL_MODEL
    threshold: float = 0.5
    use_pipeline: bool = True
    batch_size: int = 8
    force_cleanup: bool = True
    log_level: str = "INFO"
    cache_dir: str = None

class SRSWTI0Shot:
    """SRSWTI Zero Shot Classification System"""
    
    def __init__(self, config: SRSWTIConfig = None):
        self.config = config or SRSWTIConfig()
        self.logger = logging.getLogger("SRSWTI-ZeroShot")
        self.logger.setLevel(self.config.log_level)
        self._setup_system()
        self._initialize_model()
        
    def _setup_system(self):
        """Setup system and check resources"""
        try:
            self.logger.info("Initializing SRSWTI Zero Shot Classification System...")
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
                
            self.logger.info(f"SRSWTI System will use {self.device.upper()} for processing")
            
        except Exception as e:
            self.logger.error(f"System setup failed: {str(e)}")
            raise

    def _initialize_model(self):
        """Initialize model with progress bars and careful memory management"""
        try:
            self.logger.info("Loading SRSWTI Zero Shot Classification Model...")
            
            # Show progress for tokenizer loading
            with tqdm(total=1, desc="Loading SRSWTI Tokenizer") as pbar:
                self.tokenizer = AutoTokenizer.from_pretrained(
                    self.config.internal_model,
                    cache_dir=self.config.cache_dir
                )
                pbar.update(1)
            
            # Determine appropriate dtype
            dtype = torch.float16 if self.device == "cuda" else torch.float32
            
            # Show progress for model loading
            with tqdm(total=1, desc="Loading SRSWTI Model") as pbar:
                self.model = AutoModelForSequenceClassification.from_pretrained(
                    self.config.internal_model,
                    torch_dtype=dtype,
                    cache_dir=self.config.cache_dir
                )
                pbar.update(0.5)
                
                # Move to device with progress
                self.model = self.model.to(self.device)
                pbar.update(0.5)
            
            self.model.eval()
            
            # Clean up memory
            if self.config.force_cleanup:
                gc.collect()
                if self.device == "cuda":
                    torch.cuda.empty_cache()
            
            self.logger.info("SRSWTI Model initialization complete")
            
        except Exception as e:
            self.logger.error(f"SRSWTI Model initialization failed: {str(e)}")
            self.logger.error(traceback.format_exc())
            raise

    def _manual_classify(self, text: str, candidate_labels: List[str], multi_label: bool) -> Dict:
        """Classify text with progress bar and memory management"""
        try:
            # Create sequence pairs
            sequence_pairs = [[text, f"This text is about {label}."] for label in candidate_labels]
            
            # Tokenization with progress
            with tqdm(total=2, desc="Processing") as pbar:
                inputs = self.tokenizer(
                    sequence_pairs,
                    padding=True,
                    truncation="longest_first",
                    max_length=512,
                    return_tensors="pt"
                ).to(self.device)
                pbar.update(1)
                
                # Model inference
                with torch.no_grad():
                    outputs = self.model(**inputs)
                    predictions = torch.nn.functional.softmax(outputs.logits, dim=1)
                    scores = predictions[:, 1].cpu().numpy()
                    
                    if multi_label:
                        scores = 1 / (1 + np.exp(-scores))
                    else:
                        sorted_indices = scores.argsort()[::-1]
                        candidate_labels = [candidate_labels[i] for i in sorted_indices]
                        scores = scores[sorted_indices]
                        scores = scores / scores.sum()
                pbar.update(1)
            
            result = {
                'sequence': text,
                'labels': candidate_labels,
                'scores': scores.tolist()
            }
            
            # Clean up
            if self.config.force_cleanup:
                del inputs, outputs, predictions
                if self.device == "cuda":
                    torch.cuda.empty_cache()
                    
            return result
            
        except Exception as e:
            self.logger.error(f"Classification error: {str(e)}")
            self.logger.error(traceback.format_exc())
            raise

    def _format_output(self, result: Union[Dict, List[Dict]], processing_time: float) -> Dict:
        """Format the classification output with metadata"""
        return {
            'results': result,
            'metadata': {
                'processing_time': round(processing_time, 2),
                'device': self.device.upper(),
                'model': self.config.model_name,
                'version': SRSWTI_VERSION,
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
        }      
def print_results(results: Dict):
    """Helper function to print results in a formatted way"""
    print("\nSRSWTI Zero Shot Classification Results")
    print("=" * 50)
    
    if isinstance(results['results'], list):
        for i, result in enumerate(results['results'], 1):
            print(f"\nInput {i}:")
            print(f"Text: {result['sequence']}")
            print("\nClassification Results:")
            for label, score in zip(result['labels'], result['scores']):
                print(f"  • {label:<15} {score:.2%}")
    else:
        result = results['results']
        print(f"\nText: {result['sequence']}")
        print("\nClassification Results:")
        for label, score in zip(result['labels'], result['scores']):
            print(f"  • {label:<15} {score:.2%}")
    
    print("\nSystem Information")
    print("=" * 50)
    meta = results['metadata']
    print(f"• Model:           {meta['model']}")
    print(f"• Version:         {meta['version']}")
    print(f"• Device:          {meta['device']}")
    print(f"• Processing Time: {meta['processing_time']} seconds")
    print(f"• Timestamp:       {meta['timestamp']}")
    
def main():
    try:
        # Initialize with explicit configuration
        config = SRSWTIConfig(
            device="cpu",  # Explicitly set device
            use_pipeline=False,
            force_cleanup=True,
            batch_size=4,  # Reduced batch size for better memory management
            cache_dir="./model_cache"  # Cache models locally
        )
        
        print("\nInitializing SRSWTI Zero Shot Classifier...")
        classifier = SRSWTI0Shot(config)
        
        # Example tasks with progress tracking
        tasks = [
            ("Product Review", [
                "This product is amazing! Great quality and fast shipping.",
                "Terrible experience, product broke after first use."
            ], ["positive", "negative", "neutral"], False),
            
            ("News", [
                "Bitcoin reaches new all-time high as major investors increase their holdings"
            ], ["finance", "technology", "politics"], False),
            
            ("Technical Support", [
                "My application keeps crashing whenever I try to save my work"
            ], ["bug", "feature_request", "account_issue"], True)
        ]
        
        # Process each task with progress tracking
        for task_name, texts, labels, multi_label in tqdm(tasks, desc="Processing Tasks"):
            print(f"\nProcessing {task_name} Classification")
            start_time = datetime.now()
            
            for text in tqdm(texts, desc=f"Analyzing {task_name} Texts"):
                result = classifier._manual_classify(text, labels, multi_label)
                formatted_result = classifier._format_output(
                    result, 
                    (datetime.now() - start_time).total_seconds()
                )
                print_results(formatted_result)
                
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

