
from typing import List, Dict, Union, Optional
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation, TruncatedSVD
from sklearn.preprocessing import Normalizer
from bertopic import BERTopic
from keybert import KeyBERT
import logging
from abc import ABC, abstractmethod
import torch
from transformers import AutoTokenizer, AutoModel
import umap
import hdbscan

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DocumentProcessor(ABC):
    """Abstract base class for document processing"""
    
    @abstractmethod
    def preprocess(self, documents: List[str]) -> List[str]:
        """Preprocess documents"""
        pass
    
    @abstractmethod
    def fit_transform(self, documents: List[str], num_topics: int = 10):
        """Fit and transform documents"""
        pass
    
    @abstractmethod
    def transform_new_documents(self, documents: List[str]):
        """Transform new documents using fitted model"""
        pass

class SRSWTITopicModeling(DocumentProcessor):
    """
    Sophisticated Topic Modeling System with multiple backends
    Supports: BERTopic, LSA, NMF, LDA, and KeyBERT
    """
    
    def __init__(
        self,
        backend: str = 'bertopic',
        language: str = 'english',
        embedding_model: str = 'all-MiniLM-L6-v2',
        random_state: int = 42
    ):
        """
        Initialize the topic modeling system
        
        Args:
            backend (str): Choice of backend ('bertopic', 'lsa', 'nmf', 'lda', 'keybert')
            language (str): Language for text processing
            embedding_model (str): Name of the embedding model to use
            random_state (int): Random seed for reproducibility
        """
        self.backend = backend.lower()
        self.language = language
        self.embedding_model = embedding_model
        self.random_state = random_state
        self.model = None
        self.vectorizer = None
        
        # Validate backend choice
        valid_backends = ['bertopic', 'lsa', 'nmf', 'lda', 'keybert']
        if self.backend not in valid_backends:
            raise ValueError(f"Backend must be one of {valid_backends}")
        
        logger.info(f"Initializing topic modeling system with {backend} backend")
        
    def preprocess(self, documents: List[str]) -> List[str]:
        """
        Preprocess documents with basic cleaning
        
        Args:
            documents (List[str]): List of document texts
            
        Returns:
            List[str]: Preprocessed documents
        """
        # Basic preprocessing
        processed_docs = []
        for doc in documents:
            if not isinstance(doc, str):
                continue
            # Convert to lowercase
            doc = doc.lower()
            # Remove excessive whitespace
            doc = ' '.join(doc.split())
            processed_docs.append(doc)
            
        return processed_docs
    
    def _initialize_model(self, num_topics: int):
        """Initialize the specified backend model"""
        if self.backend == 'bertopic':
            # Improved BERTopic parameters for better clustering
            umap_model = umap.UMAP(
                n_neighbors=5,  # Reduced from 15 for tighter clusters
                n_components=5,
                min_dist=0.0,
                metric='cosine',
                random_state=self.random_state
            )
            hdbscan_model = hdbscan.HDBSCAN(
                min_cluster_size=2,  # Reduced from 15 for smaller datasets
                min_samples=1,
                metric='euclidean',
                cluster_selection_method='eom',
                prediction_data=True,
                gen_min_span_tree=True
            )
            self.model = BERTopic(
                language=self.language,
                embedding_model=self.embedding_model,
                umap_model=umap_model,
                hdbscan_model=hdbscan_model,
                nr_topics=num_topics,
                verbose=True,
                calculate_probabilities=True
            )
            
        elif self.backend == 'lsa':
            self.vectorizer = TfidfVectorizer(max_features=5000)
            
            # Dynamically adjust n_components based on document count
            def safe_svd_components(doc_count):
                # Ensure n_components is less than min(n_samples, n_features)
                return min(num_topics, doc_count - 1)
            
            self.safe_num_topics = safe_svd_components
            
            self.model = TruncatedSVD(
                n_components=min(num_topics, 5000),  # Initial safe default
                random_state=self.random_state
            )
            
        elif self.backend == 'nmf':
            self.vectorizer = TfidfVectorizer(max_features=5000)
            self.model = NMF(
                n_components=num_topics,
                random_state=self.random_state,
                init='nndsvd'
            )
            
        elif self.backend == 'lda':
            self.vectorizer = CountVectorizer(max_features=5000)
            self.model = LatentDirichletAllocation(
                n_components=num_topics,
                random_state=self.random_state,
                learning_method='online'
            )
            
        elif self.backend == 'keybert':
            self.model = KeyBERT(model=self.embedding_model)
    
    def fit_transform(
        self,
        documents: List[str],
        num_topics: int = 10
    ) -> Dict[str, Union[np.ndarray, List]]:
        """
        Fit the model and transform documents
        
        Args:
            documents (List[str]): List of documents to process
            num_topics (int): Number of topics to extract
            
        Returns:
            Dict containing model outputs (varies by backend)
        """
        # Preprocess documents
        processed_docs = self.preprocess(documents)
        
        # Initialize model if not already done
        if self.model is None:
            self._initialize_model(num_topics)
        
        try:
            if self.backend == 'bertopic':
                topics, probs = self.model.fit_transform(processed_docs)
                return {
                    'topic_assignments': topics,
                    'topic_probabilities': probs
                }
            
            elif self.backend == 'lsa':
                # Dynamically adjust number of components if using LSA
                doc_term_matrix = self.vectorizer.fit_transform(processed_docs)
                
                # Adjust n_components based on actual matrix dimensions
                actual_num_topics = min(num_topics, doc_term_matrix.shape[0] - 1, doc_term_matrix.shape[1])
                
                # Reinitialize model with correct number of components
                self.model = TruncatedSVD(
                    n_components=actual_num_topics,
                    random_state=self.random_state
                )
                
                # Fit and transform the model
                doc_topic_matrix = self.model.fit_transform(doc_term_matrix)
                
                return {
                    'document_topic_matrix': doc_topic_matrix,
                    'feature_names': self.vectorizer.get_feature_names_out(),
                    'actual_topics': actual_num_topics
                }
                
            elif self.backend in ['nmf']:
                # Transform documents to document-term matrix
                doc_term_matrix = self.vectorizer.fit_transform(processed_docs)
                
                # Fit and transform the model
                doc_topic_matrix = self.model.fit_transform(doc_term_matrix)
                
                return {
                    'document_topic_matrix': doc_topic_matrix,
                    'feature_names': self.vectorizer.get_feature_names_out()
                }
            
            elif self.backend == 'lda':
                # Transform documents to document-term matrix
                doc_term_matrix = self.vectorizer.fit_transform(processed_docs)
                
                # Fit and transform the model
                doc_topic_matrix = self.model.fit_transform(doc_term_matrix)
                
                # Here's where you add the perplexity calculation:
                results = {
                    'document_topic_matrix': doc_topic_matrix,
                    'feature_names': self.vectorizer.get_feature_names_out(),
                    'perplexity': self.model.perplexity(doc_term_matrix)  # Add this line
                }
                return results
                
            elif self.backend == 'keybert':
                keywords = self.model.extract_keywords(
                    processed_docs,
                    keyphrase_ngram_range=(1, 2),
                    stop_words='english',
                    use_maxsum=True,
                    nr_candidates=20,
                    top_n=10
                )
                return {'keywords': keywords}
                
        except Exception as e:
            logger.error(f"Error in fit_transform: {str(e)}")
            raise
    
    def transform_new_documents(
        self,
        documents: List[str]
    ) -> Dict[str, Union[np.ndarray, List]]:
        """
        Transform new documents using the fitted model
        
        Args:
            documents (List[str]): New documents to transform
            
        Returns:
            Dict containing model outputs for new documents
        """
        if self.model is None:
            raise ValueError("Model must be fitted before transforming new documents")
        
        processed_docs = self.preprocess(documents)
        
        try:
            if self.backend == 'bertopic':
                topics, probs = self.model.transform(processed_docs)
                return {
                    'topic_assignments': topics,
                    'topic_probabilities': probs
                }
                
            elif self.backend in ['lsa', 'nmf', 'lda']:
                doc_term_matrix = self.vectorizer.transform(processed_docs)
                doc_topic_matrix = self.model.transform(doc_term_matrix)
                return {'document_topic_matrix': doc_topic_matrix}
                
            elif self.backend == 'keybert':
                keywords = self.model.extract_keywords(processed_docs)
                return {'keywords': keywords}
                
        except Exception as e:
            logger.error(f"Error in transform_new_documents: {str(e)}")
            raise
    
    def get_topic_words(
        self,
        topic_id: Optional[int] = None,
        top_n: int = 10
    ) -> Union[List[str], Dict[int, List[str]]]:
        """
        Get the most representative words for topics
        
        Args:
            topic_id (int, optional): Specific topic ID to get words for
            top_n (int): Number of top words to return per topic
            
        Returns:
            List[str] or Dict[int, List[str]]: Top words for specified topic(s)
        """
        if self.model is None:
            raise ValueError("Model must be fitted before getting topic words")
        
        try:
            if self.backend == 'bertopic':
                if topic_id is not None:
                    return self.model.get_topic(topic_id)[:top_n]
                return self.model.get_topics()
                
            elif self.backend in ['lsa', 'nmf', 'lda']:
                feature_names = self.vectorizer.get_feature_names_out()
                
                if topic_id is not None:
                    topic = self.model.components_[topic_id]
                    top_words_idx = topic.argsort()[:-top_n-1:-1]
                    return [feature_names[i] for i in top_words_idx]
                
                topics_dict = {}
                for idx, topic in enumerate(self.model.components_):
                    top_words_idx = topic.argsort()[:-top_n-1:-1]
                    topics_dict[idx] = [feature_names[i] for i in top_words_idx]
                return topics_dict
                
            elif self.backend == 'keybert':
                logger.warning("KeyBERT doesn't support topic word extraction")
                return []
                
        except Exception as e:
            logger.error(f"Error in get_topic_words: {str(e)}")
            raise

# Example usage and testing code (commented out)
def display_model_results(results, backend, documents, topic_model):
    """Helper function to display complete results for each model"""
    print(f"\n{'='*80}")
    print(f"Testing {backend.upper()} Backend")
    print(f"{'='*80}\n")
    
    try:
        if backend == 'bertopic':
            topics = results['topic_assignments']
            probs = results['topic_probabilities']
            
            print("BERTopic Results:")
            print("-" * 40)
            
            # Show complete topic distribution
            unique_topics = sorted(set(topics))
            print("\nComplete Topic Distribution:")
            for topic in unique_topics:
                docs_in_topic = [i for i, t in enumerate(topics) if t == topic]
                count = len(docs_in_topic)
                print(f"\nTopic {topic}: {count} documents")
                print("Documents in this topic:")
                for doc_idx in docs_in_topic:
                    print(f"Doc {doc_idx}: {documents[doc_idx][:100]}...")  # Show first 100 chars
            
            # Show all topic probabilities
            print("\nComplete Topic Probabilities:")
            for idx, prob in enumerate(probs):
                print(f"\nDocument {idx} probabilities:")
                for topic_idx, topic_prob in enumerate(prob):
                    print(f"Topic {topic_idx}: {topic_prob:.4f}")
                
        elif backend in ['lsa', 'nmf', 'lda']:
            print(f"{backend.upper()} Results:")
            print("-" * 40)
            
            doc_topic_matrix = results['document_topic_matrix']
            
            if backend == 'nmf':
                print(f"\nReconstruction Error: {topic_model.model.reconstruction_err_:.4f}\n")
            elif backend == 'lda':
                print(f"\nPerplexity: {results.get('perplexity', 'N/A')}\n")
            
            print("Topics:\n")
            # Get and display all topic words
            all_topics = topic_model.get_topic_words()
            for topic_id, words in all_topics.items():
                print(f"\nTopic {topic_id}:")
                print(", ".join(words))
            
            # Show complete document-topic distribution
            print("\nComplete Document-Topic Distributions:")
            for idx in range(doc_topic_matrix.shape[0]):
                print(f"\nDocument {idx}:")
                print(f"Text: {documents[idx][:100]}...")  # Show first 100 chars
                print("Topic Distribution:")
                for topic_idx in range(doc_topic_matrix.shape[1]):
                    weight = doc_topic_matrix[idx, topic_idx]
                    print(f"Topic {topic_idx}: {weight:.4f}")
                dominant_topic = np.argmax(doc_topic_matrix[idx])
                print(f"Dominant Topic: {dominant_topic} (Weight: {doc_topic_matrix[idx, dominant_topic]:.4f})")
                
        elif backend == 'keybert':
            print("KeyBERT Results:")
            print("-" * 40)
            
            keywords = results['keywords']
            
            # Show keywords for all documents
            print("\nDocument-Level Keywords:")
            for idx, doc_keywords in enumerate(keywords):
                print(f"\nDocument {idx}:")
                print(f"Text: {documents[idx][:100]}...")  # Show first 100 chars
                if isinstance(doc_keywords, list):
                    for keyword, score in doc_keywords:
                        print(f"{keyword} ({score:.3f})", end=', ')
                else:
                    print(doc_keywords)
                print()
            
    except Exception as e:
        print(f"\nError processing {backend}:")
        print(f"Error type: {type(e).__name__}")
        print(f"Error message: {str(e)}")

def test_topic_modeling_comprehensive():
    """
    Comprehensive test suite for all topic modeling backends with complete outputs
    """
    # Sample documents with clear themes
    documents = [
        # Technology (0-4)
        "Python programming is essential for data science and machine learning applications",
        "Deep learning models use neural networks for complex pattern recognition",
        "Cloud computing enables scalable infrastructure for big data processing",
        "Cybersecurity protects systems from malicious attacks and data breaches",
        "Artificial intelligence is transforming automation and decision making",
        
        # Healthcare (5-9)
        "Medical research advances treatment options for chronic diseases",
        "Preventive healthcare focuses on maintaining wellness through lifestyle",
        "Telemedicine provides remote access to healthcare services globally",
        "Vaccination programs prevent the spread of infectious diseases",
        "Mental health awareness promotes psychological well-being",
        
        # Environment (10-14)
        "Renewable energy sources reduce carbon emissions and climate impact",
        "Ocean conservation protects marine ecosystems and biodiversity",
        "Sustainable agriculture promotes environmentally friendly farming",
        "Recycling programs help manage waste and conserve resources",
        "Forest preservation maintains biodiversity and reduces global warming",
        
        # Business (15-19)
        "Digital transformation revolutionizes business operations and strategy",
        "Market analysis helps companies make informed decisions",
        "Supply chain optimization improves efficiency and reduces costs",
        "Customer experience drives brand loyalty and business growth",
        "Innovation management facilitates organizational development"
    ]
    
    # Test each backend
    backends = ['bertopic', 'lsa', 'nmf', 'lda', 'keybert']
    num_topics = 4  # We have 4 main themes
    
    for backend in backends:
        try:
            # Initialize model
            topic_model = SRSWTITopicModeling(
                backend=backend,
                language='english',
                embedding_model='all-MiniLM-L6-v2',
                random_state=42
            )
            
            # Fit and transform documents
            results = topic_model.fit_transform(documents, num_topics=num_topics)
            
            # Display complete results
            display_model_results(results, backend, documents, topic_model)
            
            print("\nProcessing completed successfully for", backend)
            print("-" * 75)
            
        except Exception as e:
            print(f"\nError processing {backend} backend:")
            print(f"Error type: {type(e).__name__}")
            print(f"Error message: {str(e)}")
            continue

if __name__ == "__main__":
    test_topic_modeling_comprehensive()