from transformers import pipeline
import torch
import logging
import os
from tqdm import tqdm
from rich.console import Console
from rich.progress import Progress
from rich.logging import RichHandler
from typing import List, Dict, Union
import time
import datetime

class SRSWTIZeroShot:
    """SRSWTI Zero-Shot Classification System"""
    
    def __init__(self, device: str = None, model_name: str = "SRSWTI-ZeroShot-v1", batch_size: int = None):
        """
        Initialize the SRSWTI Zero-Shot Classification System
        
        :param device: Device to run the model on (cuda, mps, cpu)
        :param model_name: Name of the zero-shot classification model
        :param batch_size: Number of texts to process in a single batch
        """
        # Create logs directory if it doesn't exist
        logs_dir = os.path.join(os.path.dirname(__file__), 'logs')
        os.makedirs(logs_dir, exist_ok=True)
        
        # Configure logging with rich and file logging
        log_filename = os.path.join(logs_dir, f'srswti_zeroshot_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.log')
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s [%(levelname)s] SRSWTI-ZeroShot: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            handlers=[
                RichHandler(rich_tracebacks=True),
                logging.FileHandler(log_filename)
            ]
        )
        self.logger = logging.getLogger("SRSWTI-ZeroShot")
        self.console = Console()
        
        # Determine device
        if device is None:
            device = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"
        
        self.batch_size = batch_size
        self.device = device
        
        self.logger.info(f"Initializing SRSWTI Zero-Shot Classifier on {device} with batch size {batch_size}")
        self.console.print(f"[bold green]Initializing Zero-Shot Classifier on {device} with batch size {batch_size}[/bold green]")
        
        # Load Hugging Face Zero-Shot Classification Pipeline
        self.classifier = pipeline(
            "zero-shot-classification", 
            model="facebook/bart-large-mnli", 
            device=device,
            batch_size=batch_size
        )
        
    def classify_text(self, text: str, candidate_labels: List[str], multi_label: bool = False) -> Dict[str, float]:
        """
        Classify the input text into one or more labels using a zero-shot classifier.
        
        :param text: The input text to classify
        :param candidate_labels: A list of possible categories for classification
        :param multi_label: Boolean indicating if multiple labels can be assigned
        :return: Dictionary with labels and corresponding scores
        """
        start_time = time.time()
        
        try:
            result = self.classifier(text, candidate_labels, multi_label=multi_label)
            
            classification_time = time.time() - start_time
            
            self.logger.info(f"Classification completed in {classification_time:.4f} seconds")
            
            return {label: score for label, score in zip(result["labels"], result["scores"])}
        
        except Exception as e:
            self.logger.error(f"Classification error: {str(e)}")
            self.console.print(f"[bold red]❌ Classification Error: {str(e)}[/bold red]")
            return {}

    def process_tasks(self, tasks: List[Dict[str, Union[str, List[str], bool]]]):
        """
        Process multiple classification tasks with progress tracking
        
        :param tasks: List of classification tasks
        """
        self.logger.info("Starting SRSWTI Zero-Shot Classification Tasks")
        self.console.print("[bold blue]🔍 Starting Zero-Shot Classification Tasks[/bold blue]")
        
        for task_item in tasks:
            self.console.print(f"\n[bold green]Task: {task_item['name']}[/bold green]")
            self.logger.info(f"Processing task: {task_item['name']}")
            
            # Process texts in batches
            for i in range(0, len(task_item['texts']), self.batch_size):
                batch_texts = task_item['texts'][i:i+self.batch_size]
                
                for text in batch_texts:
                    self.console.print(f"\n[yellow]Text:[/yellow] {text}")
                    classification_result = self.classify_text(
                        text, 
                        task_item['labels'], 
                        multi_label=task_item.get("multi_label", False)
                    )
                    
                    self.console.print("[bold blue]Classification Result:[/bold blue]")
                    for label, score in classification_result.items():
                        self.console.print(f"{label}: [green]{score:.4f}[/green]")

if __name__ == "__main__":
    # Define tasks for zero-shot classification with more complex, real-life scenarios
    tasks = [
        {
            "name": "E-commerce Product Reviews",
            "texts": [
                "The noise-cancelling headphones exceeded my expectations. Crystal clear audio and incredible battery life, but the price point is a bit steep for budget-conscious consumers.",
                "Purchased a smart home security system that completely failed during a critical moment. Unreliable sensors and poor customer support made this a nightmare.",
                "This ergonomic office chair is a game-changer for remote workers. Excellent lumbar support, adjustable features, and helps prevent back pain during long coding sessions.",
                "Sustainable clothing line that talks about ethical production, but the quality doesn't match the premium pricing. Fabric feels thin and wears out quickly.",
                "Cutting-edge smartphone with revolutionary AI camera, but the battery drain is significant. Innovative features come at the cost of practical daily use.",
                "Medical-grade air purifier that genuinely improved my family's respiratory health during wildfire season. Worth every penny for those with allergies or air quality concerns."
            ],
            "labels": ["highly_positive", "positive", "neutral", "critical", "negative", "highly_negative"],
            "multi_label": True
        },
        {
            "name": "Global Technology & Innovation News",
            "texts": [
                "OpenAI's latest language model demonstrates unprecedented natural language understanding, raising both excitement and ethical concerns about AI's potential societal impact.",
                "Breakthrough in quantum computing: researchers at MIT develop a stable 1000-qubit processor that could revolutionize cryptography and scientific simulations.",
                "Climate tech startup secures $250 million in funding to develop carbon capture technology that promises to remove atmospheric CO2 at industrial scales.",
                "Geopolitical tensions escalate as major tech companies navigate complex international regulations and data sovereignty challenges.",
                "Artificial intelligence shows promising results in early-stage medical diagnosis, potentially transforming healthcare delivery and patient outcomes.",
                "Blockchain technology moves beyond cryptocurrency, with innovative applications in supply chain transparency, voting systems, and decentralized finance."
            ],
            "labels": ["artificial_intelligence", "quantum_computing", "climate_tech", "geopolitics", "healthcare_innovation", "blockchain", "economic_impact"],
            "multi_label": True
        },
        {
            "name": "Enterprise Software Support",
            "texts": [
                "Critical security vulnerability discovered in our enterprise resource planning system. Immediate patch required to prevent potential data breaches.",
                "Performance bottleneck in our cloud-native microservices architecture is causing intermittent system-wide latency issues during peak load times.",
                "Machine learning model deployment pipeline experiencing unexpected training data drift, leading to decreased prediction accuracy.",
                "Complex integration challenge between legacy financial systems and modern API-driven platforms, requiring comprehensive architectural redesign.",
                "Compliance team flagged potential GDPR and CCPA violations in our current data handling processes. Urgent review and remediation needed.",
                "Kubernetes cluster experiencing resource allocation inefficiencies, resulting in increased operational costs and suboptimal container orchestration."
            ],
            "labels": ["security_vulnerability", "performance_issue", "machine_learning", "system_integration", "compliance", "infrastructure", "architectural_challenge"],
            "multi_label": True
        },
        {
            "name": "Professional Workplace Sentiment",
            "texts": [
                "Implementing a four-day work week has dramatically improved team morale, productivity, and work-life balance. Employees report feeling more engaged and less burned out.",
                "Ongoing restructuring and uncertainty about job security are creating significant psychological strain among team members.",
                "Innovative remote collaboration tools and asynchronous communication strategies have transformed our global team's effectiveness.",
                "Persistent skills gap in emerging technologies is creating challenges in talent acquisition and professional development.",
                "Company's commitment to diversity, equity, and inclusion initiatives is generating positive cultural transformation and attracting top-tier talent.",
                "Increasing burnout rates in high-pressure tech industries highlight the critical need for comprehensive mental health support and sustainable work practices."
            ],
            "labels": ["positive_transformation", "workplace_stress", "innovation", "talent_development", "cultural_change", "mental_health", "organizational_challenges"],
            "multi_label": True
        }
    ]
    # Initialize and run SRSWTI Zero-Shot Classifier
    srswti_classifier = SRSWTIZeroShot()
    srswti_classifier.process_tasks(tasks)
