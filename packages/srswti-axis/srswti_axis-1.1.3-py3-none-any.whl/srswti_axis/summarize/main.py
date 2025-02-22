import os
import warnings
import torch
import time
from transformers import pipeline

class SRSWTISummarizer:
    # Disable built-in progress bars for Hugging Face Transformers.
    os.environ["TRANSFORMERS_NO_TQDM"] = "1"

    # Mitigate semaphore warnings by setting the sharing strategy.
    try:
        torch.multiprocessing.set_sharing_strategy('file_system')
    except Exception as e:
        warnings.warn(f"Could not set sharing strategy: {e}")

    # Enable cuDNN benchmark for potential speedup if using GPU.
    if torch.cuda.is_available():
        torch.backends.cudnn.benchmark = True

    # Mapping models with SRSWTI abbreviations.
    MODEL_MAPPING = {
        # Lightweight Models (<200MB)
        "SRSWTI-LW1": {
            "name": "t5-small",
            "description": "Lightweight summarization model (T5-small)",
            "size": "60MB",
            "best_for": ["quick inference", "mobile", "low-resource environments"]
        },
        "SRSWTI-LW2": {
            "name": "sshleifer/distilbart-cnn-12-6", 
            "description": "Distilled BART model for efficient summarization",
            "size": "150MB", 
            "best_for": ["production", "fast processing"]
        },
        "SRSWTI-LW3": {
            "name": "google/pegasus-xsum",
            "description": "Lightweight extreme summarization model",
            "size": "180MB",
            "best_for": ["headlines", "short summaries"]
        },

        # Medium Models (200MB-500MB)
        "SRSWTI-MD1": {
            "name": "t5-base",
            "description": "Medium-sized T5 summarization model",
            "size": "220MB", 
            "best_for": ["general-purpose", "balanced performance"]
        },
        "SRSWTI-MD2": {
            "name": "facebook/bart-large-cnn",
            "description": "Medium BART model for news and article summarization",
            "size": "400MB",
            "best_for": ["news", "professional content"]
        },
        "SRSWTI-MD3": {
            "name": "google/pegasus-cnn_dailymail",
            "description": "Pegasus model trained on CNN/Daily Mail dataset",
            "size": "450MB", 
            "best_for": ["news articles", "balanced summarization"]
        },

        # Heavy Models (500MB-1GB)
        "SRSWTI-HV1": {
            "name": "facebook/bart-large-cnn",
            "description": "Heavy BART model for comprehensive summarization",
            "size": "400MB",
            "best_for": ["detailed summaries", "complex texts"]
        },
        "SRSWTI-HV2": {
            "name": "t5-large",
            "description": "Large T5 model for high-quality summarization",
            "size": "800MB",
            "best_for": ["complex content", "high-quality summaries"]
        },
        "SRSWTI-HV3": {
            "name": "google/pegasus-large",
            "description": "State-of-the-art large Pegasus model",
            "size": "2.2GB", 
            "best_for": ["highest-quality summaries", "advanced NLP tasks"]
        }
    }

    def __init__(self, device=None, batch_size=8, use_fp16=False):
        """
        Initializes the summarizer.
        
        Args:
            device (int or str, optional): Device id. Defaults to GPU (0) if available, otherwise CPU (-1).
            batch_size (int, optional): Batch size for processing. Defaults to 8.
            use_fp16 (bool, optional): Whether to use half-precision for inference. Only effective on GPU.
        """
        if device is None:
            device = 0 if torch.cuda.is_available() else -1
        self.device = device
        self.batch_size = batch_size
        self.use_fp16 = use_fp16
        self.summarizer = None
        self.current_model = None

    @staticmethod
    def log(message, level="INFO"):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"[SRSWTI {level}] {timestamp} - {message}")

    @staticmethod
    def timing(operation, duration):
        print(f"[SRSWTI METRICS] Operation: {operation} - Duration: {duration:.2f} seconds")

    def load_summarizer(self, model_key):
        if model_key not in self.MODEL_MAPPING:
            raise ValueError(f"[SRSWTI ERROR] Invalid model configuration: {model_key}")
        
        # Only load if a different model is requested
        if self.current_model != model_key:
            model_info = self.MODEL_MAPPING[model_key]
            self.log(f"Initializing {model_key} summarization engine on device {self.device}...")
            self.summarizer = pipeline(
                "summarization", 
                model=model_info["name"], 
                tokenizer=model_info["name"], 
                framework="pt", 
                device=self.device
            )
            if self.use_fp16 and self.device != -1:
                # Convert model to half-precision for faster inference on GPU
                self.summarizer.model.half()
            self.current_model = model_key
            self.log(f"Engine {model_key} initialized successfully")
        
        return self.summarizer

    def summarize_text(self, text, model_key="SRSWTI-LW2", min_length=30, max_length=200):
        start_time = time.time()
        self.log(f"Starting single text summarization with {model_key}")
        
        summarizer = self.load_summarizer(model_key)
        summary = summarizer(text, min_length=min_length, max_length=max_length, truncation=True)
        
        duration = time.time() - start_time
        self.timing("Single text summarization", duration)
        return summary[0]['summary_text']

    def summarize_batch(self, texts, model_key="SRSWTI-LW2", min_length=30, max_length=200):
        start_time = time.time()
        self.log(f"Starting batch summarization with {model_key}")
        
        summarizer = self.load_summarizer(model_key)
        summaries = summarizer(
            texts, 
            min_length=min_length, 
            max_length=max_length, 
            truncation=True, 
            batch_size=self.batch_size
        )
        
        duration = time.time() - start_time
        self.timing("Batch summarization", duration)
        return [item['summary_text'] for item in summaries]

    def run_examples(self):
        # Enhanced batch texts with approximately 400-500 tokens each
        batch_texts = [
            """The evolution of artificial intelligence and machine learning has transformed numerous industries, reshaping how businesses operate and how we interact with technology. From healthcare diagnostics to autonomous vehicles, AI applications continue to expand their reach and capabilities. Deep learning models, particularly in computer vision and natural language processing, have achieved unprecedented accuracy levels. This progress has been driven by advances in hardware acceleration, availability of massive datasets, and innovations in neural network architectures. However, challenges remain in areas such as explainability, bias mitigation, and ethical considerations. As AI systems become more sophisticated, questions about accountability and transparency become increasingly important. The integration of AI with traditional systems requires careful consideration of security implications, resource optimization, and scalability factors. Organizations must balance the potential benefits of AI adoption with implementation costs and necessary infrastructure upgrades.""",
            
            """Climate change represents one of the most pressing challenges of our time, with far-reaching implications for ecosystems, economies, and human societies worldwide. Recent studies have documented accelerating glacial melt, rising sea levels, and increasing frequency of extreme weather events. The interconnected nature of climate systems means that changes in one region can have cascading effects globally. Scientists have observed shifts in precipitation patterns, ocean acidification, and biodiversity loss. These changes impact agriculture, water resources, and food security. International efforts to address climate change have led to agreements like the Paris Accord, though implementation challenges persist. The transition to renewable energy sources, development of carbon capture technologies, and adoption of sustainable practices are crucial components of climate action strategies. Economic considerations, technological innovation, and policy frameworks all play vital roles in addressing this complex challenge.""",
            
            """Quantum computing represents a paradigm shift in computational capabilities, leveraging quantum mechanical phenomena to perform certain calculations exponentially faster than classical computers. The fundamental unit, the qubit, can exist in multiple states simultaneously through superposition, enabling parallel processing at an unprecedented scale. Current research focuses on improving qubit coherence times, reducing error rates, and developing quantum error correction techniques. Potential applications span cryptography, drug discovery, financial modeling, and optimization problems. The quantum computing landscape includes various competing technologies, from superconducting circuits to trapped ions and topological qubits. Major technology companies and research institutions are racing to achieve quantum supremacy and develop practical quantum applications. The field faces significant challenges in scaling qubit systems while maintaining coherence and minimizing environmental interference.""",
            
            """The impact of social media on modern society extends far beyond simple communication, fundamentally altering how information spreads, communities form, and public opinion develops. These platforms have become powerful tools for political movements, business marketing, and social change. Research indicates significant effects on mental health, privacy concerns, and information quality. The algorithmic curation of content creates echo chambers and filter bubbles, potentially reinforcing existing beliefs and biases. Social media platforms face increasing scrutiny over content moderation, data privacy, and their role in spreading misinformation. The evolution of these platforms continues with the integration of advanced features like augmented reality, virtual commerce, and decentralized networks. Understanding the long-term sociological and psychological impacts of social media remains a crucial research area.""",
            
            """Biotechnology advances are revolutionizing medicine, agriculture, and environmental conservation through innovations in genetic engineering, synthetic biology, and molecular diagnostics. CRISPR gene editing technology has opened new possibilities for treating genetic disorders and developing resilient crops. The field encompasses various applications, from personalized medicine based on genetic profiles to biofuel production using engineered microorganisms. Recent developments include breakthrough therapies for previously untreatable conditions, sustainable material production through biological processes, and novel approaches to environmental remediation. The intersection of biotechnology with artificial intelligence is accelerating drug discovery and protein design. Ethical considerations surrounding genetic modification, biosafety protocols, and equitable access to biotechnology benefits remain important discussion points.""",
            
            """The emergence of blockchain technology has introduced new paradigms for decentralized systems, extending far beyond its initial cryptocurrency applications. This distributed ledger technology enables transparent, immutable record-keeping with applications in supply chain management, digital identity verification, and secure voting systems. Smart contracts automate complex transactions without intermediaries, potentially revolutionizing legal and financial processes. The technology continues to evolve with solutions addressing scalability, energy efficiency, and interoperability between different blockchain networks. Enterprise adoption focuses on private and consortium blockchains, while public blockchains explore new consensus mechanisms and layer-2 scaling solutions. The integration of blockchain with Internet of Things devices creates new possibilities for autonomous systems and secure data exchange. Regulatory frameworks are developing to address challenges in cryptocurrency markets and blockchain-based financial services."""
        ]

        # Process examples with timing metrics
        self.log("Starting summarization examples")
        
        # Single text summarization examples
        for model_type in ["SRSWTI-LW3", "SRSWTI-HV1"]:
            self.log(f"Processing single texts with {model_type}")
            for idx, text in enumerate(batch_texts[:2], 1):
                summary = self.summarize_text(text, model_key=model_type)
                print(f"\nText {idx} Summary:\n{summary}")

        # Batch processing example
        self.log("Starting batch processing")
        batch_summaries = self.summarize_batch(batch_texts, model_key="SRSWTI-LW2")
        for idx, summary in enumerate(batch_summaries, 1):
            print(f"\nBatch Summary {idx}:\n{summary}")

def main():
    summarizer = SRSWTISummarizer(device=0, batch_size=8, use_fp16=True)
    summarizer.run_examples()

if __name__ == '__main__':
    main()
