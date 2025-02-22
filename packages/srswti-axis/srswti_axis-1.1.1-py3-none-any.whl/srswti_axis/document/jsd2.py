from typing import List, Dict, Optional, Union, Tuple
import numpy as np
from scipy.spatial.distance import cosine
from sentence_transformers import SentenceTransformer
import logging
from abc import ABC, abstractmethod
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
import torch
import torch.nn.functional as F

class DocumentProcessor(ABC):
    """Base class for document processing operations."""
    @abstractmethod
    def process(self, 
                documents: List[str],
                reference_doc: Optional[str] = None,
                threshold: float = 0.5) -> Dict[str, Union[float, List[str]]]:
        """Abstract method for processing documents."""
        pass

class SRSWTIDivergenceV2(DocumentProcessor):
    def __init__(self, 
                embedding_model: str = 'all-MiniLM-L6-v2',
                semantic_dims: int = 128,
                semantic_temperature: float = 0.1,
                n_topics: int = 10,
                min_df: int = 2):
        """Initialize with parameters."""
        # Initialize base parameters
        self.model_name = embedding_model
        self._encoder = None
        self.semantic_dims = semantic_dims
        self.semantic_temperature = semantic_temperature
        self._projection_matrix = None
        
        # NMF parameters
        self.n_topics = n_topics
        self.min_df = min_df
        self._vectorizer = None
        self._nmf_model = None
        self._topic_vectors = None
        
        # Download NLTK data
        try:
            nltk.data.find('corpora/stopwords')
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('stopwords')
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

    def process(self, 
                documents: List[str],
                reference_doc: Optional[str] = None,
                threshold: float = 0.5) -> Dict[str, Union[float, List[str]]]:
        """
        Process a list of documents and calculate their divergence.
        
        Args:
            documents: List of documents to analyze
            reference_doc: Optional reference document
            threshold: Divergence threshold
            
        Returns:
            Dictionary with analysis results
        """
        # Initialize NMF with all documents
        self._initialize_nmf(documents)
        
        results = {
            'scores': [],
            'similar_texts': [],
            'divergent_texts': []
        }
        
        try:
            ref_doc = reference_doc if reference_doc else documents[0]
            
            for doc in documents:
                if doc == ref_doc:
                    continue
                    
                score = self.calculate_divergence(ref_doc, doc)
                results['scores'].append(score)
                
                if score <= threshold:
                    results['similar_texts'].append(doc)
                else:
                    results['divergent_texts'].append(doc)
                    
            return results
            
        except Exception as e:
            logging.error(f"Failed to process documents: {e}")
            raise

    def _initialize_nmf(self, texts: List[str]):
        """Initialize NMF model."""
        if self._vectorizer is None:
            self._vectorizer = TfidfVectorizer(
                max_features=1000,
                min_df=self.min_df,
                stop_words='english',
                token_pattern=r'\b\w+\b'
            )
            tfidf_matrix = self._vectorizer.fit_transform(texts)
            
            self._nmf_model = NMF(
                n_components=self.n_topics,
                init='nndsvd',
                random_state=42
            )
            self._topic_vectors = self._nmf_model.fit_transform(tfidf_matrix)

    def _create_semantic_distribution(self, text: str) -> Tuple[np.ndarray, float]:
        """Create semantic distribution."""
        sentences = sent_tokenize(text)
        if len(sentences) == 0:
            sentences = [text]
        
        embeddings = self.encoder.encode(sentences)
        embeddings = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)
        
        if not hasattr(self, 'semantic_anchors'):
            rng = np.random.RandomState(42)
            self.semantic_anchors = rng.normal(0, 1, (self.semantic_dims, embeddings.shape[1]))
            self.semantic_anchors = self.semantic_anchors / np.linalg.norm(
                self.semantic_anchors, axis=1, keepdims=True)
        
        similarities = np.dot(embeddings, self.semantic_anchors.T)
        logits = similarities / self.semantic_temperature
        logits = logits - np.max(logits, axis=1, keepdims=True)
        probs = np.exp(logits)
        distribution = probs / np.sum(probs, axis=1, keepdims=True)
        final_dist = np.mean(distribution, axis=0)
        
        sent_entropy = -np.sum(final_dist * np.log2(final_dist + 1e-10))
        word_complexity = len(text.split()) / max(len(sentences), 1)
        complexity = (0.7 * sent_entropy / np.log2(self.semantic_dims) + 
                     0.3 * min(1.0, word_complexity / 20.0))
        
        return final_dist, complexity

    def _improved_jensen_shannon(self, p: np.ndarray, q: np.ndarray) -> float:
        """Compute Jensen-Shannon divergence."""
        eps = 1e-10
        p = np.maximum(p, eps)
        q = np.maximum(q, eps)
        
        p = p / np.sum(p)
        q = q / np.sum(q)
        
        m = 0.5 * (p + q)
        
        def safe_kl(x, y):
            valid_mask = x > eps
            safe_x = x[valid_mask]
            safe_y = y[valid_mask]
            return np.sum(safe_x * (np.log2(safe_x) - np.log2(safe_y)))
        
        kl_p_m = safe_kl(p, m)
        kl_q_m = safe_kl(q, m)
        
        jsd = 0.5 * (kl_p_m + kl_q_m)
        return np.sqrt(min(1.0, max(0.0, jsd)))

    def _get_topic_distribution(self, text: str) -> np.ndarray:
        """Get topic distribution."""
        tfidf_vector = self._vectorizer.transform([text])
        topic_dist = self._nmf_model.transform(tfidf_vector)[0]
        topic_dist = np.maximum(topic_dist, 1e-10)
        return topic_dist / topic_dist.sum()

    def calculate_divergence(self, 
                           text1: str, 
                           text2: str, 
                           return_components: bool = False) -> Union[float, Dict[str, float]]:
        """Calculate divergence between two texts."""
        try:
            # Get distributions
            dist1, complexity1 = self._create_semantic_distribution(text1)
            dist2, complexity2 = self._create_semantic_distribution(text2)
            topic_dist1 = self._get_topic_distribution(text1)
            topic_dist2 = self._get_topic_distribution(text2)
            
            # Calculate metrics
            cosine_sim = max(0.0, min(1.0, 1 - cosine(
                self.encoder.encode([text1])[0],
                self.encoder.encode([text2])[0]
            )))
            
            semantic_jsd = self._improved_jensen_shannon(dist1, dist2)
            topic_jsd = self._improved_jensen_shannon(topic_dist1, topic_dist2)
            
            # Calculate weights
            avg_complexity = (complexity1 + complexity2) / 2.0
            semantic_weight = 0.6 + 0.2 * (1 - avg_complexity)
            topic_weight = 1.0 - semantic_weight
            
            # Calculate final score
            final_score = (semantic_weight * (0.7 * (1 - cosine_sim) + 0.3 * semantic_jsd) +
                          topic_weight * topic_jsd)
            
            if return_components:
                return {
                    'divergence_score': float(final_score),
                    'cosine_similarity': float(cosine_sim),
                    'semantic_jsd': float(semantic_jsd),
                    'topic_jsd': float(topic_jsd),
                    'entropy_p': float(-np.sum(dist1 * np.log2(dist1 + 1e-10))),
                    'entropy_q': float(-np.sum(dist2 * np.log2(dist2 + 1e-10))),
                    'text_complexity_1': float(complexity1),
                    'text_complexity_2': float(complexity2),
                    'semantic_weight': float(semantic_weight),
                    'topic_weight': float(topic_weight)
                }
            
            return float(final_score)
            
        except Exception as e:
            logging.error(f"Failed to calculate divergence: {e}")
            raise

    def get_topic_words(self, top_n: int = 10) -> List[List[str]]:
        """Get top words for each topic."""
        if self._nmf_model is None or self._vectorizer is None:
            raise ValueError("NMF model not initialized. Process some texts first.")
            
        feature_names = np.array(self._vectorizer.get_feature_names_out())
        topics = []
        
        for topic_idx, topic in enumerate(self._nmf_model.components_):
            top_words_idx = topic.argsort()[:-top_n-1:-1]
            topics.append(feature_names[top_words_idx].tolist())
            
        return topics

    
if __name__ == "__main__":
    test_texts = {
        'research_paper': {
            'base': """
            Recent advances in deep learning have revolutionized the field of computer vision. Convolutional Neural Networks (CNNs) 
            have demonstrated remarkable performance in image classification, object detection, and semantic segmentation tasks. 
            These architectures leverage hierarchical feature extraction, where early layers capture basic visual elements like edges 
            and textures, while deeper layers learn increasingly complex representations. Transfer learning techniques have further 
            enhanced the practical applicability of these models, allowing practitioners to achieve state-of-the-art results with 
            limited training data through fine-tuning pre-trained networks.
            """,
            'similar': """
            The evolution of neural networks has transformed visual computing paradigms. Deep learning approaches, particularly 
            the application of Convolutional Neural Networks, have achieved unprecedented accuracy in computer vision tasks. 
            These deep architectures excel at automatically learning relevant features from raw image data, with initial layers 
            detecting basic patterns and subsequent layers identifying complex visual concepts. The advent of transfer learning 
            has made these powerful models more accessible, enabling researchers to adapt pre-trained networks for specific 
            applications with minimal additional training data.
            """,
            'different': """
            Quantum computing represents a fundamental shift in computational paradigms. Unlike classical computers that operate 
            on binary bits, quantum computers utilize quantum bits or qubits, which can exist in multiple states simultaneously 
            through superposition. This property, combined with quantum entanglement, enables quantum computers to perform certain 
            calculations exponentially faster than traditional computers. Recent developments in quantum error correction and 
            hardware stability have brought us closer to achieving practical quantum supremacy.
            """
        },
        'medical_article': {
            'base': """
            The human microbiome plays a crucial role in maintaining overall health and disease prevention. The diverse community 
            of microorganisms inhabiting the human gut influences everything from metabolism to immune system function. Recent 
            research has revealed strong connections between gut microbiota composition and various health conditions, including 
            obesity, inflammatory bowel disease, and even mental health disorders. Understanding these complex interactions has 
            led to new therapeutic approaches, including targeted probiotics and fecal microbiota transplantation.
            """,
            'similar': """
            The complex ecosystem of microorganisms within the human digestive system has emerged as a critical factor in health 
            maintenance. Scientists have discovered that the gut microbiome's composition significantly impacts numerous 
            physiological processes, from digestive efficiency to immune response. Growing evidence suggests that alterations in 
            gut bacterial populations are linked to various medical conditions, spanning metabolic disorders to psychological 
            health. These insights have spawned innovative treatments focusing on microbiome manipulation through probiotics 
            and bacterial transplant procedures.
            """,
            'different': """
            Renewable energy technologies have made significant strides in recent years, with solar and wind power becoming 
            increasingly cost-competitive with traditional fossil fuels. Advances in photovoltaic cell efficiency and wind 
            turbine design have dramatically reduced the levelized cost of electricity generation. Energy storage solutions, 
            particularly lithium-ion batteries, have also evolved to address intermittency issues. These developments are 
            reshaping the global energy landscape and accelerating the transition to sustainable power sources.
            """
        },
        'environmental_report': {
            'base': """
            Climate change poses unprecedented challenges to global ecosystems and biodiversity. Rising global temperatures 
            have led to significant alterations in weather patterns, causing more frequent extreme weather events and 
            disrupting natural habitats. Arctic ice melt has accelerated, threatening polar ecosystems and contributing to 
            sea level rise. Meanwhile, ocean acidification is severely impacting marine life, particularly coral reefs and 
            shellfish populations. These changes are creating cascading effects throughout food webs and ecosystems worldwide.
            """,
            'similar': """
            Global warming has emerged as a critical threat to Earth's biological systems and species diversity. The steady 
            increase in average temperatures worldwide has triggered substantial changes in climate patterns, resulting in 
            more severe weather phenomena and habitat destruction. Polar regions are experiencing rapid ice loss, endangering 
            local wildlife and coastal communities through rising sea levels. The increasing acidity of ocean waters poses a 
            grave danger to marine ecosystems, especially affecting coral communities and calcifying organisms.
            """,
            'different': """
            The development of artificial general intelligence (AGI) presents both unprecedented opportunities and challenges 
            for humanity. Current research focuses on developing systems that can match or exceed human-level reasoning 
            across multiple domains. Key challenges include ensuring alignment with human values, maintaining controllability, 
            and addressing potential ethical concerns. The development of robust safety protocols and governance frameworks 
            will be crucial as these technologies advance.
            """
        },
        'business_analysis': {
            'base': """
            Digital transformation has fundamentally altered the business landscape, forcing companies to reimagine their 
            operational models and customer engagement strategies. E-commerce platforms have revolutionized retail, while 
            cloud computing has enabled unprecedented scalability and flexibility. Data analytics and artificial intelligence 
            are providing deeper insights into customer behavior and optimizing business processes. Companies that fail to 
            adapt to this digital revolution risk becoming obsolete in an increasingly competitive market.
            """,
            'similar': """
            The digital revolution has reshaped how businesses operate and interact with consumers. Traditional business 
            models are being disrupted as organizations embrace digital technologies and online platforms. Cloud-based 
            solutions have transformed IT infrastructure, offering scalable and cost-effective alternatives to traditional 
            systems. Advanced analytics and machine learning are enabling companies to make data-driven decisions and 
            personalize customer experiences. This technological shift is creating a new paradigm in business operations.
            """,
            'different': """
            Advances in genetic engineering, particularly CRISPR-Cas9 technology, have opened new frontiers in medical 
            treatment and biological research. This precise gene-editing tool allows scientists to modify DNA sequences 
            with unprecedented accuracy, offering potential treatments for genetic disorders and improving crop resilience. 
            However, ethical considerations and safety concerns surrounding genetic modification continue to generate 
            significant debate in the scientific community.
            """
        }
    }
    # Initialize analyzer
    analyzer = SRSWTIDivergenceV2(
        semantic_dims=128,
        semantic_temperature=0.1,
        n_topics=5,
        min_df=1
    )
    
    print("\nTesting Enhanced Semantic Divergence Analysis with NMF:")
    print("=" * 80)
    
    # First, collect all texts for NMF initialization
    all_texts = []
    for category in test_texts.values():
        all_texts.extend(category.values())
    
    # Initialize NMF with all texts
    analyzer._initialize_nmf(all_texts)
    
    # Print topic information
    print("\nDiscovered Topics:")
    print("-" * 40)
    topics = analyzer.get_topic_words(top_n=5)
    for idx, topic_words in enumerate(topics):
        print(f"Topic {idx + 1}: {', '.join(topic_words)}")
    print("=" * 80)
    
    # Test each category
    for category_name, texts in test_texts.items():
        print(f"\nTesting {category_name.upper()} category:")
        print("-" * 40)
        
        # Compare similar texts
        similar_score = analyzer.calculate_divergence(
            texts['base'], 
            texts['similar'],
            return_components=True
        )
        print(f"Similar texts divergence components:")
        for k, v in similar_score.items():
            if isinstance(v, float):
                print(f"  {k}: {v:.4f}")
        
        # Compare different texts
        print(f"\nDifferent texts divergence components:")
        different_score = analyzer.calculate_divergence(
            texts['base'],
            texts['different'],
            return_components=True
        )
        for k, v in different_score.items():
            if isinstance(v, float):
                print(f"  {k}: {v:.4f}")
        
        # Print topic distributions
        print("\nTopic Distribution Analysis:")
        base_topics = analyzer._get_topic_distribution(texts['base'])
        similar_topics = analyzer._get_topic_distribution(texts['similar'])
        different_topics = analyzer._get_topic_distribution(texts['different'])
        
        # Get top topics for each text
        def get_top_topics(dist, n=3):
            top_indices = np.argsort(dist)[-n:][::-1]
            return [(i+1, dist[i]) for i in top_indices]
        
        print("\nTop Topics (Topic #, Weight):")
        print(f"Base text: {get_top_topics(base_topics)}")
        print(f"Similar text: {get_top_topics(similar_topics)}")
        print(f"Different text: {get_top_topics(different_topics)}")
        
        print("=" * 80)
    
    # Print summary statistics
    print("\nSummary Statistics:")
    print("-" * 40)
    
    similar_scores = []
    different_scores = []
    topic_divergences = []
    semantic_divergences = []
    
    for texts in test_texts.values():
        sim_score = analyzer.calculate_divergence(texts['base'], texts['similar'])
        diff_score = analyzer.calculate_divergence(texts['base'], texts['different'])
        similar_scores.append(sim_score)
        different_scores.append(diff_score)
        
        # Get component scores
        sim_components = analyzer.calculate_divergence(texts['base'], texts['similar'], return_components=True)
        topic_divergences.append(sim_components['topic_jsd'])
        semantic_divergences.append(sim_components['semantic_jsd'])
    
    print(f"Average Similar Text Score: {np.mean(similar_scores):.4f} (±{np.std(similar_scores):.4f})")
    print(f"Average Different Text Score: {np.mean(different_scores):.4f} (±{np.std(different_scores):.4f})")
    print(f"Average Topic Divergence: {np.mean(topic_divergences):.4f} (±{np.std(topic_divergences):.4f})")
    print(f"Average Semantic Divergence: {np.mean(semantic_divergences):.4f} (±{np.std(semantic_divergences):.4f})")
    print("\nScore Ranges:")
    print(f"Similar Texts: {min(similar_scores):.4f} - {max(similar_scores):.4f}")
    print(f"Different Texts: {min(different_scores):.4f} - {max(different_scores):.4f}")
    
    print("\nAnalysis Complete!")