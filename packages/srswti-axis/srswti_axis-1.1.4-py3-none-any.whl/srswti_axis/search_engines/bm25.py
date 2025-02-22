# from typing import List, Dict, Tuple, Optional
# import numpy as np
# from scipy.sparse import csr_matrix
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# from sentence_transformers import SentenceTransformer
# import spacy
# import logging

# logger = logging.getLogger(__name__)

# class SRSWTISearchEngine:
#     def __init__(self, embedding_model: str = 'srswti-neural-embedder-v1'):
#         model_mapping = {'srswti-neural-embedder-v1': 'all-MiniLM-L6-v2'}
#         actual_model = model_mapping.get(embedding_model, embedding_model)
#         self.embedder = SentenceTransformer(actual_model)
#         self.nlp = spacy.load('en_core_web_sm')
#         self.tfidf = TfidfVectorizer(ngram_range=(1, 2))
#         self.bm25_k1 = 1.5
#         self.bm25_b = 0.75
#         logger.info("SRSWTI Search Engine initialized successfully")

#     def preprocess_text(self, text: str) -> str:
#         doc = self.nlp(text.lower())
#         tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
#         return " ".join(tokens)

#     def calculate_bm25_scores(self, query: str, documents: List[str]) -> np.ndarray:
#         processed_docs = [self.preprocess_text(doc) for doc in documents]
#         processed_query = self.preprocess_text(query)
        
#         tfidf_matrix = self.tfidf.fit_transform(processed_docs)
#         doc_lengths = np.sum(tfidf_matrix > 0, axis=1).A1
#         avg_doc_length = np.mean(doc_lengths)
        
#         query_vector = self.tfidf.transform([processed_query])
#         feature_names = self.tfidf.get_feature_names_out()
        
#         scores = np.zeros(len(documents))
#         query_terms = processed_query.split()
        
#         for term in query_terms:
#             if term in feature_names:
#                 term_idx = feature_names.tolist().index(term)
#                 tf = tfidf_matrix[:, term_idx].toarray().flatten()
#                 idf = self.tfidf.idf_[term_idx]
#                 numerator = tf * (self.bm25_k1 + 1)
#                 denominator = tf + self.bm25_k1 * (1 - self.bm25_b + self.bm25_b * doc_lengths / avg_doc_length)
#                 scores += idf * (numerator / denominator)
        
#         return scores

#     def calculate_proximity_scores(self, query: str, documents: List[str]) -> np.ndarray:
#         """Enhanced proximity scoring to reflect term closeness more effectively"""
#         query_terms = set(self.preprocess_text(query).split())
#         scores = np.zeros(len(documents))
        
#         for idx, doc in enumerate(documents):
#             doc_tokens = self.preprocess_text(doc).split()
#             positions = {term: [] for term in query_terms}
            
#             # Record positions of query terms in the document
#             for pos, token in enumerate(doc_tokens):
#                 if token in query_terms:
#                     positions[token].append(pos)
            
#             # Calculate minimum distances between query terms
#             if len([pos for pos_list in positions.values() if pos_list]) > 1:  # At least two terms present
#                 distances = []
#                 terms_present = [t for t, pos_list in positions.items() if pos_list]
#                 for i in range(len(terms_present)):
#                     for j in range(i + 1, len(terms_present)):
#                         pos1 = positions[terms_present[i]]
#                         pos2 = positions[terms_present[j]]
#                         min_dist = min(abs(p1 - p2) for p1 in pos1 for p2 in pos2)
#                         distances.append(min_dist)
                
#                 if distances:
#                     avg_dist = np.mean(distances)
#                     # Higher score for closer terms, exponential decay for distance
#                     scores[idx] = np.exp(-avg_dist / 10.0)  # Decay factor tuned for sensitivity
        
#         return scores

#     def hybrid_search(self, 
#                       query: str, 
#                       documents: List[str],
#                       weights: Dict[str, float] = None) -> List[Tuple[int, float]]:
#         """Updated hybrid search to mimic Cohere-like ranking"""
#         if weights is None:
#             weights = {'bm25': 0.35, 'semantic': 0.45, 'proximity': 0.20}  # Adjusted for balance
        
#         logger.info("Starting hybrid search pipeline...")
        
#         # BM25 Component
#         bm25_scores = self.calculate_bm25_scores(query, documents)
        
#         # Neural Component
#         query_embedding = self.embedder.encode([query])[0]
#         doc_embeddings = self.embedder.encode(documents)
#         semantic_scores = cosine_similarity([query_embedding], doc_embeddings)[0]
        
#         # Proximity Component
#         proximity_scores = self.calculate_proximity_scores(query, documents)
        
#         # Normalize scores to [0, 1] with a softer approach
#         def normalize(scores):
#             max_score = np.max(scores)
#             min_score = np.min(scores)
#             if max_score == min_score:
#                 return np.ones_like(scores) if max_score > 0 else np.zeros_like(scores)
#             return (scores - min_score) / (max_score - min_score)
        
#         bm25_scores = normalize(bm25_scores)
#         semantic_scores = normalize(semantic_scores)
#         proximity_scores = normalize(proximity_scores)
        
#         # Combine scores with weights
#         final_scores = (
#             weights['bm25'] * bm25_scores +
#             weights['semantic'] * semantic_scores +
#             weights['proximity'] * proximity_scores
#         )
        
#         # Apply a slight boost to emphasize relevance (mimicking Cohere’s smooth decay)
#         final_scores = final_scores * (1 + np.clip(semantic_scores, 0, 1) * 0.1)  # Semantic boost
        
#         # Sort and return results
#         ranked_indices = np.argsort(-final_scores)
#         logger.info("SRSWTI hybrid search completed successfully")
#         return [(idx, float(final_scores[idx])) for idx in ranked_indices]

#     def expand_query(self, query: str) -> str:
#         """SRSWTI Query Expansion Module"""
#         doc = self.nlp(query)
#         expanded_terms = set([query])
            
#         for token in doc:
#             expanded_terms.add(token.lemma_)
                
#             for synset in token._.wordnet.synsets():
#                 for lemma in synset.lemmas():
#                     expanded_terms.add(lemma.name())
            
#         logger.debug(f"SRSWTI Query Expansion: {' '.join(expanded_terms)}")
#         return ' '.join(expanded_terms)
#     def test_search_methods(self):
#         """
#         Test the search methods with sample documents and queries
#         """
#         # Sample documents
#         documents = [
#     "Carson City is the capital city of the American state of Nevada.",
#     "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",
#     "Capitalization or capitalisation in English grammar is the use of a capital letter at the start of a word. English usage varies from capitalization in other languages.",
#     "Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district.",
#     "Capital punishment has existed in the United States since beforethe United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states.",
#     "Washington, D.C. (also known as simply Washington or D.C., and officially as the District of India) is the capital of the United States. It is a federal district.",

# ]
        
#         # Test query expansion
#         test_queries = [
#             "What is the capital of the United States?"
#         ]
        
#         print("\n=== Query Expansion Test ===")
#         for query in test_queries:
#             expanded_query = self.expand_query(query)
#             print(f"Original Query: {query}")
#             print(f"Expanded Query: {expanded_query}\n")
        
#         # Test proximity-based scoring
#         print("\n=== Proximity-Based Scoring Test ===")
#         for query in test_queries:
#             proximity_scores = self.calculate_proximity_scores(query, documents)
#             print(f"Query: {query}")
#             for doc, score in zip(documents, proximity_scores):
#                 print(f"  Document: {doc}")
#                 print(f"  Proximity Score: {score:.4f}\n")
        
#         # Optional: Demonstrate full search workflow
#         print("\n=== Full Search Workflow Test ===")
#         query = "machine learning techniques"
#         expanded_query = self.expand_query(query)
#         proximity_scores = self.calculate_proximity_scores(expanded_query, documents)
        
#         # Sort documents by proximity score
#         ranked_docs = sorted(
#             zip(documents, proximity_scores), 
#             key=lambda x: x[1], 
#             reverse=True
#         )
        
#         print(f"Search Query: {query}")
#         print("Top Ranked Documents:")
#         for doc, score in ranked_docs:
#             print(f"  - {doc} (Score: {score:.4f})")


# def main():
#     # Initialize the search engine
#     search_engine = SRSWTISearchEngine()
#     # Sample documents
#     documents = [
#         "Carson City is the capital city of the American state of Nevada.",
#         "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",
#         "Capitalization or capitalisation in English grammar is the use of a capital letter at the start of a word. English usage varies from capitalization in other languages.",
#         "Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district.",
#         "Capital punishment has existed in the United States since beforethe United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states.",
#         "Washington, D.C. (also known as simply Washington or D.C., and officially as the District of India) is the capital of the United States. It is a federal district.",
#         "Sacramento is the capital city of California, located in the northern part of the state.",
#         "Austin serves as the capital of Texas and is known for its vibrant music scene.",
#         "Tokyo is the capital city of Japan and one of the world's largest metropolitan areas.",
#         "Paris, the capital of France, is renowned for its art, culture, and iconic landmarks.",
#         "The capital markets play a crucial role in global financial systems and economic growth.",
#         "Venture capital funding has driven innovation in the technology sector.",
#         "Capital gains tax applies to profits made from selling assets like stocks or property.",
#         "Ancient Rome was the capital of one of history's largest and most influential empires.",
#         "Beijing has served as China's capital city for several centuries."
#     ]
        
#     # Test different search queries
#     queries = [
#         "What is the capital of the United States?",
#         "Tell me about capital cities in Asia",
#         "How does capital gains tax work?",
#         "What are the different meanings of capital?",
#         "Which US states have capital cities?",
#         "Explain capital markets and venture capital",
#         "What is the capital of Nevada?",
#         "Find information about Washington DC",
#         "Tell me about capital punishment in America",
#         "What are the rules of capitalization?"
#     ]
    
#     # Test different search approaches
#     for query in queries:
#         print(f"\n=== Testing search for: '{query}' ===\n")
        
#         # # Test hybrid search with default weights
#         # print("Hybrid Search Results:")
#         # results = search_engine.hybrid_search(query, documents)
#         # for idx, score in results:
#         #     print(f"Score: {score:.4f} - {documents[idx]}")
        
#         # Test with different weights
#         custom_weights = {'bm25': 0.4, 'semantic': 0.6, 'proximity': 0.0}
#         print("\nHybrid Search with Custom Weights:")
#         results = search_engine.hybrid_search(query, documents, weights=custom_weights)
#         for idx, score in results:
#             print(f"Score: {score:.4f} - {documents[idx]}")

# if __name__ == "__main__":
#     main()

from typing import List, Dict, Tuple, Optional
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import spacy
import logging

# Logger setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s [SRSWTI-IR] %(levelname)s: %(message)s')
logger = logging.getLogger('SRSWTI-IR')

from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

class SRSWTISearchEngine:
    def __init__(self, embedding_model: str = 'srswti-neural-embedder-v1'):
        model_mapping = {'srswti-neural-embedder-v1': 'all-mpnet-base-v2'}
        actual_model = model_mapping.get(embedding_model, embedding_model)
        self.embedder = SentenceTransformer(actual_model)
        self.nlp = spacy.load('en_core_web_sm')
        self.tfidf = TfidfVectorizer(ngram_range=(1, 2))
        self.bm25_k1 = 1.5
        self.bm25_b = 0.75
        self.relevance_model = None
        self.relevance_tokenizer = None

    def preprocess_text(self, text: str) -> str:
        """SRSWTI Advanced Text Preprocessing Pipeline"""
        doc = self.nlp(text.lower())
        tokens = [
            token.lemma_ 
            for token in doc 
            if not token.is_stop and not token.is_punct
        ]
        logger.debug(f"SRSWTI Preprocessed text: {' '.join(tokens)}")
        return " ".join(tokens)

    def calculate_relevance_scores(self, query: str, documents: List[str]) -> np.ndarray:
        """Enhanced BART scoring"""
        # Load models if not already loaded
        if self.relevance_model is None:
            self.relevance_model = AutoModelForSequenceClassification.from_pretrained(
                "valhalla/distilbart-mnli-12-3"
            )
            self.relevance_tokenizer = AutoTokenizer.from_pretrained(
                "valhalla/distilbart-mnli-12-3"
            )

        scores = []
        
        # Better prompt template
        pairs = [
            f"Task: Rate document relevance to query.\nQuery: '{query}'\n"
            f"Document: '{doc}'\n"
            f"Consider: Is this a direct answer? Is it factually correct? "
            f"Does it match all query conditions?"
            for doc in documents
        ]
        
        # Batch processing
        batch_size = 8
        for i in range(0, len(pairs), batch_size):
            batch = pairs[i:i + batch_size]
            inputs = self.relevance_tokenizer(batch, padding=True, truncation=True, 
                                            max_length=512, return_tensors="pt")
            
            with torch.no_grad():
                outputs = self.relevance_model(**inputs)
                # Apply stronger sigmoid scaling
                logits = outputs.logits
                batch_scores = torch.sigmoid(3 * logits)[:, 1]  # Scale factor for better separation
                scores.extend(batch_scores.tolist())
        
        scores = np.array(scores)
        
        
        return scores

    def calculate_bm25_scores(self, query: str, documents: List[str]) -> np.ndarray:
        """BM25 scoring with error handling"""
        try:
            processed_docs = [self.preprocess_text(doc) for doc in documents]
            processed_query = self.preprocess_text(query)
            
            # Fit TF-IDF vectorizer
            tfidf_matrix = self.tfidf.fit_transform(processed_docs)
            doc_lengths = np.sum(tfidf_matrix > 0, axis=1).A1
            avg_doc_length = np.mean(doc_lengths)
            
            # Get query terms
            query_vector = self.tfidf.transform([processed_query])
            feature_names = self.tfidf.get_feature_names_out()
            
            scores = np.zeros(len(documents))
            query_terms = processed_query.split()
            
            for term in query_terms:
                if term in feature_names:
                    term_idx = feature_names.tolist().index(term)
                    tf = tfidf_matrix[:, term_idx].toarray().flatten()
                    idf = self.tfidf.idf_[term_idx]
                    
                    # BM25 formula with safety checks
                    numerator = tf * (self.bm25_k1 + 1)
                    denominator = tf + self.bm25_k1 * (1 - self.bm25_b + self.bm25_b * doc_lengths / max(avg_doc_length, 1e-10))
                    term_scores = idf * (numerator / np.maximum(denominator, 1e-10))
                    
                    scores += np.nan_to_num(term_scores, 0)
            
            return scores
            
        except Exception as e:
            logger.error(f"Error in BM25 scoring: {str(e)}")
            return np.zeros(len(documents))

    def calculate_proximity_scores(self, query: str, documents: List[str]) -> np.ndarray:
        query_terms = set(self.preprocess_text(query).split())
        scores = np.zeros(len(documents))
        
        for idx, doc in enumerate(documents):
            doc_tokens = self.preprocess_text(doc).split()
            positions = {term: [] for term in query_terms}
            
            for pos, token in enumerate(doc_tokens):
                if token in query_terms:
                    positions[token].append(pos)
            
            if len([pos for pos_list in positions.values() if pos_list]) > 1:
                distances = []
                terms_present = [t for t, pos_list in positions.items() if pos_list]
                for i in range(len(terms_present)):
                    for j in range(i + 1, len(terms_present)):
                        pos1 = positions[terms_present[i]]
                        pos2 = positions[terms_present[j]]
                        min_dist = min(abs(p1 - p2) for p1 in pos1 for p2 in pos2)
                        distances.append(min_dist)
                
                if distances:
                    avg_dist = np.mean(distances)
                    scores[idx] = np.exp(-avg_dist / 10.0)  # Smooth decay
        
        return scores


    def hybrid_search(self, query: str, documents: List[str], weights: Dict[str, float] = None) -> List[Tuple[int, float]]:
        """Hybrid search with robust score combination"""
        if weights is None:
            weights = {
                'bm25': 0.25, 
                'semantic': 0.35, 
                'proximity': 0.0,
                'relevance': 0.45  # Add weight for BART relevance scores
            }
        
        try:
            # Calculate individual scores
            bm25_scores = self.calculate_bm25_scores(query, documents)
            
            # Semantic scoring
            query_embedding = self.embedder.encode([query])[0]
            doc_embeddings = self.embedder.encode(documents)
            semantic_scores = cosine_similarity([query_embedding], doc_embeddings)[0]
            
            # Proximity scoring
            proximity_scores = self.calculate_proximity_scores(query, documents)
            
            # Only calculate relevance scores if weight is non-zero
            if weights.get('relevance', 0) > 0:
                relevance_scores = self.calculate_relevance_scores(query, documents)
                relevance_norm = self._normalize_scores(relevance_scores)
            else:
                relevance_norm = np.zeros(len(documents))
                weights['relevance'] = 0  # Ensure weight is explicitly 0
            
            # Normalize all scores
            bm25_norm = self._normalize_scores(bm25_scores)
            semantic_norm = self._normalize_scores(semantic_scores)
            proximity_norm = self._normalize_scores(proximity_scores)
            
            # Combine with weights
            final_scores = (
                weights['bm25'] * bm25_norm +
                weights['semantic'] * semantic_norm +
                weights['proximity'] * proximity_norm +
                weights['relevance'] * relevance_norm
            )

            # Final normalization to ensure scores are in [0, 1]
            final_scores = self._normalize_scores(final_scores)
            
            # Sort and return results
            ranked_indices = np.argsort(-final_scores)
            return [(idx, float(final_scores[idx])) for idx in ranked_indices]
            
        except Exception as e:
            logger.error(f"Error in hybrid search: {str(e)}")
            # Return simple ranking if error occurs
            return [(i, 0.0) for i in range(len(documents))]

    def _normalize_scores(self, scores: np.ndarray) -> np.ndarray:
        """
        Robust score normalization that handles edge cases
        """
        # Handle zero arrays
        if np.all(scores == 0):
            return np.zeros_like(scores)
        
        # Handle NaN or infinite values
        scores = np.nan_to_num(scores, nan=0.0, posinf=1.0, neginf=0.0)
        
        # Get min and max while avoiding division by zero
        min_score = np.min(scores)
        max_score = np.max(scores)
        score_range = max_score - min_score
        
        if score_range == 0:
            # If all scores are identical, return array of 0.5
            return np.full_like(scores, 0.5)
        
        # Standard min-max normalization with safety checks
        normalized = (scores - min_score) / score_range
        return normalized
        print(f"\n=== Testing search for: '{query}' ===\n")
        print("Top 3 Results:")
        results = search_engine.hybrid_search(query, documents)
        for idx, score in results[:3]:  # Only top 3
            print(f"  Document: {documents[idx]}")
            print(f"  Score: {score:.4f}")

def main():
    search_engine = SRSWTISearchEngine()
    documents = [
        "Carson City is the capital city of the American state of Nevada.",
        "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",
        "Capitalization or capitalisation in English grammar is the use of a capital letter at the start of a word. English usage varies from capitalization in other languages.",
        "Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district.",
        "Capital punishment has existed in the United States since beforethe United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states.",
        "Washington, D.C. (also known as simply Washington or D.C., and officially as the District of India) is the capital of the United States. It is a federal district.",
        "Sacramento is the capital city of California, located in the northern part of the state.",
        "Austin serves as the capital of Texas and is known for its vibrant music scene.",
        "Tokyo is the capital city of Japan and one of the world's largest metropolitan areas.",
        "Paris, the capital of France, is renowned for its art, culture, and iconic landmarks.",
        "The capital markets play a crucial role in global financial systems and economic growth.",
        "Venture capital funding has driven innovation in the technology sector.",
        "Capital gains tax applies to profits made from selling assets like stocks or property.",
        "Ancient Rome was the capital of one of history's largest and most influential empires.",
        "Beijing has served as China's capital city for several centuries."
    ]
    
    queries = [
        "What is the capital of the United States?",
        "Tell me about capital cities in Asia",
        "How does capital gains tax work?",
        "Which US states have capital cities?",
        "Explain capital markets and venture capital",
        "What is the capital of Nevada?",
        "Find information about Washington DC",
        "Tell me about capital punishment in America",
        "What are the rules of capitalization?"
    ]
    
    for query in queries:
        print(f"\n=== Testing search for: '{query}' ===\n")
        print("Top 3 Results:")
        results = search_engine.hybrid_search(query, documents, weights = {
                'bm25': 0.25, 
                'semantic': 0.75, 
                'proximity': 0.5,
                'relevance': 0.45  # Add weight for BART relevance scores
            })
        for idx, score in results[:3]:  # Only top 3
            print(f"  Document: {documents[idx]}")
            print(f"  Score: {score:.4f}")

if __name__ == "__main__":
    main()