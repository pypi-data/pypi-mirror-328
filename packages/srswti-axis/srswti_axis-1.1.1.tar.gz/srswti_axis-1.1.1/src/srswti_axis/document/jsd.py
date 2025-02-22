from typing import List, Dict, Optional, Union, Tuple
import numpy as np
from scipy.spatial.distance import cosine
from sentence_transformers import SentenceTransformer
import logging
from abc import ABC, abstractmethod
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import torch
import torch.nn.functional as F

class DocumentProcessor(ABC):
    """Base class for document processing operations."""
    @abstractmethod
    def process(self):
        pass

class SRSWTIDivergence(DocumentProcessor):
    """
    Enhanced Semantic Divergence Analysis with robust JSD calculation.
    Handles semantic distance calculations between texts using fixed-dimension
    semantic spaces and stable probability distributions.
    """
    
    def __init__(self, 
                embedding_model: str = 'all-MiniLM-L6-v2',
                semantic_dims: int = 128,
                semantic_temperature: float = 0.1,
                projection_seed: int = 42):
        """
        Initialize the divergence analyzer with enhanced parameters.
        
        Args:
            embedding_model: Name of the SentenceTransformer model to use
            semantic_dims: Fixed dimensionality for semantic space projection
            semantic_temperature: Controls distribution sharpness
            projection_seed: Seed for random projection matrix
        """
        self.model_name = embedding_model
        self._encoder = None
        self.semantic_dims = semantic_dims
        self.semantic_temperature = semantic_temperature
        self.projection_seed = projection_seed
        self._projection_matrix = None
        
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt')
    
    @property
    def encoder(self) -> SentenceTransformer:
        """Lazy load the sentence transformer model."""
        if self._encoder is None:
            try:
                self._encoder = SentenceTransformer(self.model_name)
            except Exception as e:
                logging.error(f"Failed to load encoder model: {e}")
                raise
        return self._encoder
    
    def _get_projection_matrix(self, input_dims: int) -> np.ndarray:
        """
        Get or create orthogonal projection matrix for dimension reduction.
        Uses QR decomposition for better projection properties.
        
        Args:
            input_dims: Input dimensionality from encoder
            
        Returns:
            Orthogonal projection matrix
        """
        if self._projection_matrix is None or self._projection_matrix.shape[0] != input_dims:
            np.random.seed(self.projection_seed)
            random_matrix = np.random.randn(input_dims, self.semantic_dims)
            q, r = np.linalg.qr(random_matrix)
            self._projection_matrix = q[:, :self.semantic_dims]
        return self._projection_matrix

    def _create_semantic_distribution(self, text: str) -> Tuple[np.ndarray, float]:
        """
        Create semantic distribution focusing on meaning preservation.
        """
        # Get sentence embeddings
        sentences = sent_tokenize(text)
        if len(sentences) == 0:
            sentences = [text]
        
        # Get embeddings and normalize
        embeddings = self.encoder.encode(sentences)
        embeddings = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)
        
        # Create fixed-size distribution (using semantic dimensions)
        K = self.semantic_dims  # e.g., 32
        
        # Create semantic anchors if not exists
        if not hasattr(self, 'semantic_anchors'):
            rng = np.random.RandomState(42)
            self.semantic_anchors = rng.normal(0, 1, (K, embeddings.shape[1]))
            self.semantic_anchors = self.semantic_anchors / np.linalg.norm(
                self.semantic_anchors, axis=1, keepdims=True)
        
        # Project embeddings onto semantic space
        similarities = np.dot(embeddings, self.semantic_anchors.T)  # (n_sentences, K)
        
        # Create probability distribution
        logits = similarities / self.semantic_temperature
        logits = logits - np.max(logits, axis=1, keepdims=True)  # numerical stability
        probs = np.exp(logits)
        distribution = probs / np.sum(probs, axis=1, keepdims=True)
        
        # Aggregate to fixed-size distribution
        final_dist = np.mean(distribution, axis=0)
        
        # Calculate meaningful complexity
        sent_entropy = -np.sum(final_dist * np.log2(final_dist + 1e-10))
        word_complexity = len(text.split()) / max(len(sentences), 1)
        complexity = (0.7 * sent_entropy / np.log2(K) + 
                    0.3 * min(1.0, word_complexity / 20.0))
        
        return final_dist, complexity

    def _stable_softmax(self, x: np.ndarray, axis: int = -1) -> np.ndarray:
        """
        Compute softmax with improved numerical stability.
        
        Args:
            x: Input array
            axis: Axis along which to compute softmax
            
        Returns:
            Softmax probabilities
        """
        x_max = np.max(x, axis=axis, keepdims=True)
        exp_x = np.exp((x - x_max) / self.semantic_temperature)
        return exp_x / np.sum(exp_x, axis=axis, keepdims=True)

    def _calculate_semantic_complexity(self, 
                                    distribution: np.ndarray, 
                                    word_coherence: float) -> float:
        """
        Calculate semantic complexity using distribution entropy and word coherence.
        
        Args:
            distribution: Probability distribution
            word_coherence: Word-level semantic coherence score
            
        Returns:
            Combined complexity score
        """
        # Calculate distribution entropy
        valid_dist = np.maximum(distribution, 1e-10)
        valid_dist = valid_dist / np.sum(valid_dist)
        entropy = -np.sum(valid_dist * np.log2(valid_dist))
        
        # Normalize entropy
        max_entropy = np.log2(len(distribution))
        entropy_ratio = entropy / max_entropy if max_entropy > 0 else 0.5
        
        # Combine with word coherence
        return 0.7 * entropy_ratio + 0.3 * word_coherence

    def _improved_jensen_shannon(self, p: np.ndarray, q: np.ndarray) -> float:
        """
        Compute Jensen-Shannon divergence with guaranteed numerical stability.
        """
        # Ensure non-zero probabilities
        eps = 1e-10
        p = np.maximum(p, eps)
        q = np.maximum(q, eps)
        
        # Normalize
        p = p / np.sum(p)
        q = q / np.sum(q)
        
        # Compute midpoint
        m = 0.5 * (p + q)
        
        # Compute KL divergences safely
        def safe_kl(x, y):
            # Only compute where x is non-zero
            valid_mask = x > eps
            safe_x = x[valid_mask]
            safe_y = y[valid_mask]
            return np.sum(safe_x * (np.log2(safe_x) - np.log2(safe_y)))
        
        kl_p_m = safe_kl(p, m)
        kl_q_m = safe_kl(q, m)
        
        # Compute final JSD
        jsd = 0.5 * (kl_p_m + kl_q_m)
        
        # Return normalized square root
        return np.sqrt(min(1.0, max(0.0, jsd)))

    def calculate_divergence(self, text1: str, text2: str, 
                            return_components: bool = False) -> Union[float, Dict[str, float]]:
        # Get distributions and complexities
        dist1, complexity1 = self._create_semantic_distribution(text1)
        dist2, complexity2 = self._create_semantic_distribution(text2)
        
        # Calculate metrics
        cosine_sim = max(0.0, min(1.0, 1 - cosine(
            self.encoder.encode([text1])[0], 
            self.encoder.encode([text2])[0]
        )))
        
        jsd = self._improved_jensen_shannon(dist1, dist2)
        
        # Calculate weights based on complexities
        avg_complexity = (complexity1 + complexity2) / 2.0
        semantic_diff = jsd  # Use JSD directly for weight adjustment
        
        # Dynamic weight calculation
        cosine_weight = 0.7 - 0.2 * avg_complexity - 0.1 * semantic_diff
        cosine_weight = np.clip(cosine_weight, 0.4, 0.8)
        jsd_weight = 1.0 - cosine_weight
        
        # Final score
        score = cosine_weight * (1 - cosine_sim) + jsd_weight * jsd
        
        if return_components:
            return {
                'divergence_score': float(score),
                'cosine_similarity': float(cosine_sim),
                'jensen_shannon_divergence': float(jsd),
                'entropy_p': float(-np.sum(dist1 * np.log2(dist1 + 1e-10))),
                'entropy_q': float(-np.sum(dist2 * np.log2(dist2 + 1e-10))),
                'text_complexity_1': float(complexity1),
                'text_complexity_2': float(complexity2),
                'cosine_weight': float(cosine_weight),
                'jsd_weight': float(jsd_weight)
            }
        
        return float(score)

    def compare_texts(self, 
                     texts: List[str], 
                     reference_text: Optional[str] = None,
                     threshold: float = 0.5) -> Dict[str, Union[float, List[str]]]:
        """Compare multiple texts against a reference."""
        results = {
            'scores': [],
            'similar_texts': [],
            'divergent_texts': []
        }
        
        try:
            ref_text = reference_text if reference_text else texts[0]
            
            for text in texts:
                if text == ref_text:
                    continue
                    
                score = self.calculate_divergence(ref_text, text)
                results['scores'].append(score)
                
                if score <= threshold:
                    results['similar_texts'].append(text)
                else:
                    results['divergent_texts'].append(text)
                    
            return results
            
        except Exception as e:
            logging.error(f"Failed to compare texts: {e}")
            raise

    def process(self, 
                documents: List[str],
                reference_doc: Optional[str] = None,
                threshold: float = 0.5) -> Dict[str, Union[float, List[str]]]:
        """Process documents according to DocumentProcessor interface."""
        return self.compare_texts(documents, reference_doc, threshold)
    
if __name__ == "__main__":
    # Test cases
    test_texts = {
        'cat': {
            'base': "Cats are adorable domestic pets. They have soft fur and independent personalities.",
            'similar': "Felines are charming household companions. These animals possess silky coats and autonomous behaviors.",
            'different': "Dogs are loyal animals that love to play fetch. They are known for their energetic nature."
        },
        'ml': {
            'base': "Machine learning is a subset of artificial intelligence that focuses on algorithms learning from data.",
            'similar': "Deep learning, an advanced branch of machine learning, utilizes complex neural network architectures.",
            'different': "Mechanical engineering involves designing and creating physical machines."
        },
        'environment': {
            'base': "Climate change is a significant global challenge affecting ecosystems and human societies.",
            'similar': "Global warming poses critical risks to biodiversity and sustainable development.",
            'different': "Economic policies in developing countries focus on industrial growth and infrastructure."
        },
        'literature': {
            'base': "Shakespeare's plays explore complex human emotions and societal dynamics.",
            'similar': "Classic literature often delves into profound psychological and social themes.",
            'different': "Modern technology has revolutionized communication and information sharing."
        },
        'health': {
            'base': "Nutrition plays a crucial role in maintaining overall physical and mental well-being.",
            'similar': "A balanced diet is essential for optimal human health and disease prevention.",
            'different': "Quantum computing is transforming computational capabilities in scientific research."
        }
    }
    
    # Initialize analyzer
    analyzer = SRSWTIDivergence()
    
    print("Testing Semantic Divergence Analysis:")
    print("-" * 50)
    
    # Test each category
    for category, texts in test_texts.items():
        print(f"\nTesting {category.upper()} category:")
        
        # Compare similar texts
        similar_score = analyzer.calculate_divergence(
            texts['base'], 
            texts['similar'],
            return_components=True
        )
        print(f"Similar texts divergence components:")
        for k, v in similar_score.items():
            print(f"  {k}: {v:.4f}")
            
        # Compare different texts
        different_score = analyzer.calculate_divergence(
            texts['base'],
            texts['different'],
            return_components=True
        )
        print(f"\nDifferent texts divergence components:")
        for k, v in different_score.items():
            print(f"  {k}: {v:.4f}")
        print("-" * 50)