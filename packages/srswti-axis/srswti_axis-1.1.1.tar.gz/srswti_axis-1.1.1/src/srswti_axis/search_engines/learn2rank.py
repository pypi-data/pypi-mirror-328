import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
from sklearn.preprocessing import StandardScaler
from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import TfidfVectorizer

@dataclass
class Document:
    """Document with features and relevance score"""
    text: str
    features: np.ndarray
    relevance: float = 0.0

class FeatureExtractor:
    """Extracts features for Learning to Rank"""
    def __init__(self, embedding_model: str = 'srswti-neural-embedder-v1'):
        # Map SRSWTI model alias to the actual model
        model_mapping = {
            'srswti-neural-embedder-v1': 'all-mpnet-base-v2'
        }
        actual_model = model_mapping.get(embedding_model, embedding_model)
        self.embedder = SentenceTransformer(actual_model)
        self.tfidf = TfidfVectorizer()
        self.scaler = StandardScaler()
        
    def extract_features(self, query: str, documents: List[str]) -> np.ndarray:
        """Extract features for ranking"""
        features = []
        
        # TF-IDF features
        tfidf_matrix = self.tfidf.fit_transform(documents)
        query_tfidf = self.tfidf.transform([query])
        tfidf_scores = (query_tfidf @ tfidf_matrix.T).toarray()[0]
        
        # Semantic features
        query_embedding = self.embedder.encode([query])[0]
        doc_embeddings = self.embedder.encode(documents)
        semantic_scores = np.inner(query_embedding, doc_embeddings)
        
        # Document length features
        doc_lengths = [len(doc.split()) for doc in documents]
        
        # Combine all features
        for idx in range(len(documents)):
            doc_features = [
                tfidf_scores[idx],                    # TF-IDF similarity
                semantic_scores[idx],                 # Semantic similarity
                doc_lengths[idx],                     # Document length
                doc_lengths[idx] / np.mean(doc_lengths)  # Relative length
            ]
            features.append(doc_features)
            
        features = np.array(features)
        return self.scaler.fit_transform(features)

class PointwiseRanker(nn.Module):
    """Neural network for pointwise ranking"""
    def __init__(self, input_dim: int):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(input_dim, 64),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(32, 1),
            nn.Sigmoid()
        )
        
    def forward(self, x):
        return self.model(x)

class PairwiseRanker(nn.Module):
    """Neural network for pairwise ranking using RankNet approach"""
    def __init__(self, input_dim: int):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(input_dim, 64),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 1)
        )
        
    def forward(self, x1, x2):
        score1 = self.model(x1)
        score2 = self.model(x2)
        return torch.sigmoid(score1 - score2)

class ListwiseRanker(nn.Module):
    """Neural network for listwise ranking using ListNet approach"""
    def __init__(self, input_dim: int):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(input_dim, 64),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 1)
        )
        
    def forward(self, x):
        scores = self.model(x)
        return torch.softmax(scores, dim=0)

class SRSWTIHilbertSearch:
    """Complete Learning to Rank system with all three approaches"""
    def __init__(self, approach: str = 'pointwise'):
        self.feature_extractor = FeatureExtractor()
        self.approach = approach
        self.model = None
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        
    def train(self, 
             queries: List[str],
             documents: List[List[str]],
             relevance_scores: List[List[float]],
             epochs: int = 100):
        """Train the ranking model"""
        # Extract features for all query-document pairs
        all_features = []
        all_scores = []
        
        for query, docs, scores in zip(queries, documents, relevance_scores):
            features = self.feature_extractor.extract_features(query, docs)
            all_features.append(features)
            all_scores.append(scores)
            
        # Initialize appropriate model based on approach
        input_dim = all_features[0].shape[1]
        if self.approach == 'pointwise':
            self.model = PointwiseRanker(input_dim).to(self.device)
            self._train_pointwise(all_features, all_scores, epochs)
        elif self.approach == 'pairwise':
            self.model = PairwiseRanker(input_dim).to(self.device)
            self._train_pairwise(all_features, all_scores, epochs)
        else:  # listwise
            self.model = ListwiseRanker(input_dim).to(self.device)
            self._train_listwise(all_features, all_scores, epochs)
    
    def _train_pointwise(self, features: List[np.ndarray], scores: List[List[float]], epochs: int):
        """Train pointwise ranking model"""
        optimizer = optim.Adam(self.model.parameters())
        criterion = nn.MSELoss()
        
        for epoch in range(epochs):
            total_loss = 0
            for feat_batch, score_batch in zip(features, scores):
                x = torch.FloatTensor(feat_batch).to(self.device)
                y = torch.FloatTensor(score_batch).reshape(-1, 1).to(self.device)
                
                optimizer.zero_grad()
                pred = self.model(x)
                loss = criterion(pred, y)
                loss.backward()
                optimizer.step()
                
                total_loss += loss.item()
                
            if (epoch + 1) % 10 == 0:
                print(f'Epoch {epoch+1}/{epochs}, Loss: {total_loss/len(features):.4f}')
    
    def _train_pairwise(self, features: List[np.ndarray], scores: List[List[float]], epochs: int):
        """Train pairwise ranking model"""
        optimizer = optim.Adam(self.model.parameters())
        criterion = nn.BCELoss()
        
        for epoch in range(epochs):
            total_loss = 0
            for feat_batch, score_batch in zip(features, scores):
                # Generate document pairs
                n_docs = len(feat_batch)
                for i in range(n_docs):
                    for j in range(i + 1, n_docs):
                        x1 = torch.FloatTensor(feat_batch[i]).to(self.device)
                        x2 = torch.FloatTensor(feat_batch[j]).to(self.device)
                        
                        # Target: 1 if doc1 should rank higher than doc2
                        target = torch.FloatTensor([1.0 if score_batch[i] > score_batch[j] else 0.0]).to(self.device)
                        
                        optimizer.zero_grad()
                        pred = self.model(x1.unsqueeze(0), x2.unsqueeze(0))
                        
                        # Ensure pred and target have the same shape
                        pred = pred.view_as(target)
                        
                        loss = criterion(pred, target)
                        loss.backward()
                        optimizer.step()
                        
                        total_loss += loss.item()
                        
            if (epoch + 1) % 10 == 0:
                print(f'Epoch {epoch+1}/{epochs}, Loss: {total_loss/len(features):.4f}')
    
    def _train_listwise(self, features: List[np.ndarray], scores: List[List[float]], epochs: int):
        """Train listwise ranking model"""
        optimizer = optim.Adam(self.model.parameters())
        
        for epoch in range(epochs):
            total_loss = 0
            for feat_batch, score_batch in zip(features, scores):
                x = torch.FloatTensor(feat_batch).to(self.device)
                y = torch.FloatTensor(score_batch).to(self.device)
                
                # Convert scores to probabilities
                y = torch.softmax(y, dim=0)
                
                optimizer.zero_grad()
                pred = self.model(x)
                
                # ListNet uses cross entropy between two probability distributions
                loss = -torch.sum(y * torch.log(pred + 1e-10))
                loss.backward()
                optimizer.step()
                
                total_loss += loss.item()
                
            if (epoch + 1) % 10 == 0:
                print(f'Epoch {epoch+1}/{epochs}, Loss: {total_loss/len(features):.4f}')
    
    def rank_documents(self, query: str, documents: List[str]) -> List[Tuple[int, float]]:
        """Rank documents using trained model"""
        features = self.feature_extractor.extract_features(query, documents)
        x = torch.FloatTensor(features).to(self.device)
        
        with torch.no_grad():
            if self.approach == 'pointwise':
                scores = self.model(x).cpu().numpy().flatten()
            elif self.approach == 'pairwise':
                # For pairwise, compute scores by comparing with all other documents
                scores = np.zeros(len(documents))
                for i in range(len(documents)):
                    wins = 0
                    for j in range(len(documents)):
                        if i != j:
                            pred = self.model(
                                x[i].unsqueeze(0),
                                x[j].unsqueeze(0)
                            ).item()
                            if pred > 0.5:
                                wins += 1
                    scores[i] = wins
            else:  # listwise
                scores = self.model(x).cpu().numpy().flatten()
        
        # Sort and return indices with scores
        ranked_indices = np.argsort(-scores)
        return [(idx, scores[idx]) for idx in ranked_indices]
    
# import numpy as np
# from typing import List, Dict
# from datetime import datetime

# def create_test_dataset() -> Dict:
#     """Create sample dataset for testing"""
#     # Sample documents from different topics
#     documents = [
#         # Technology documents
#         "Machine learning is transforming how we approach artificial intelligence and computational problems.",
#         "Python programming language is known for its simplicity and readability.",
#         "Deep neural networks require significant computational resources for training.",
#         "Cloud computing enables scalable and flexible software solutions.",
        
#         # Sports documents
#         "The basketball team won the championship after an intense overtime game.",
#         "Soccer players need to maintain peak physical condition throughout the season.",
#         "Tennis requires both mental focus and physical agility to excel.",
        
#         # Food documents
#         "Italian cuisine is known for its use of fresh ingredients and simple preparations.",
#         "Sushi preparation requires years of training to master proper technique.",
#         "Traditional Mexican dishes often incorporate complex spice combinations.",
        
#         # Science documents
#         "probability and statistics challenges our understanding of reality at the smallest scales.",
#         "Climate change is affecting global weather patterns and ecosystems.",
#         "DNA sequencing has revolutionized our understanding of genetics."
#     ]
    
#     # Training queries with relevance scores (0-1 scale)
#     training_queries = [
#         {
#             "query": "machine learning artificial intelligence",
#             "relevance": [0.95, 0.3, 0.8, 0.4, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.1, 0.2]
#         },
#         {
#             "query": "sports physical training",
#             "relevance": [0.2, 0.1, 0.2, 0.1, 0.8, 0.9, 0.85, 0.1, 0.2, 0.1, 0.1, 0.1, 0.1]
#         },
#         {
#             "query": "traditional food preparation",
#             "relevance": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.9, 0.95, 0.9, 0.1, 0.1, 0.1]
#         },
#         {
#             "query": "scientific research advances",
#             "relevance": [0.4, 0.1, 0.3, 0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.9, 0.85, 0.9]
#         }
#     ]
    
#     # Test queries for evaluation
#     test_queries = [
#         "latest developments in AI and machine learning",
#         "professional sports training techniques",
#         "authentic cuisine and cooking methods",
#         "modern scientific discoveries",
#         "programming and software development",
#         "physical fitness and athletics"
#     ]
    
#     return {
#         "documents": documents,
#         "training_queries": training_queries,
#         "test_queries": test_queries
#     }

# def evaluate_ranking(ranker, query: str, documents: List[str], 
#                     expected_top_k: List[int] = None) -> Dict:
#     """
#     Evaluate ranking results for a single query
#     """
#     results = ranker.rank_documents(query, documents)
    
#     # Get ranked document indices and scores
#     ranked_indices = [idx for idx, _ in results]
#     scores = [score for _, score in results]
    
#     # Calculate basic metrics
#     metrics = {
#         "query": query,
#         "top_5_docs": [documents[idx] for idx in ranked_indices[:5]],
#         "top_5_scores": [scores[idx] for idx in ranked_indices[:5]]
#     }
    
#     # If we have expected rankings, calculate precision
#     if expected_top_k:
#         correct = len(set(ranked_indices[:3]).intersection(set(expected_top_k)))
#         metrics["precision_at_3"] = correct / 3
    
#     return metrics

# def test_learning_to_rank():
#     """
#     Complete test function for Learning to Rank system
#     """
#     print("Starting Learning to Rank Test...")
#     print("-" * 80)
    
#     # Load test dataset
#     dataset = create_test_dataset()
#     documents = dataset["documents"]
#     training_queries = dataset["training_queries"]
#     test_queries = dataset["test_queries"]
    
#     # Initialize rankers for all approaches
#     approaches = ['pointwise', 'pairwise', 'listwise']
#     results = {}
    
#     for approach in approaches:
#         print(f"\nTesting {approach.upper()} approach:")
#         print("-" * 40)
        
#         # Initialize and train ranker
#         ranker = SRSWTIHilbertSearch(approach=approach)
        
#         # Prepare training data
#         train_queries = [q["query"] for q in training_queries]
#         train_docs = [documents] * len(training_queries)
#         relevance_scores = [q["relevance"] for q in training_queries]
        
#         print("Training model...")
#         ranker.train(
#             queries=train_queries,
#             documents=train_docs,
#             relevance_scores=relevance_scores,
#             epochs=50  # Reduced for testing purposes
#         )
        
#         # Test on all queries
#         print("\nTesting queries:")
#         approach_results = []
        
#         for query in test_queries:
#             print(f"\nQuery: {query}")
#             result = evaluate_ranking(ranker, query, documents)
            
#             print("\nTop 3 results:")
#             for i, doc in enumerate(result["top_5_docs"][:3]):
#                 print(f"{i+1}. Score: {result['top_5_scores'][i]:.4f}")
#                 print(f"   Doc: {doc[:100]}...")
            
#             approach_results.append(result)
            
#         results[approach] = approach_results
    
#     return results

# def main():
#     """
#     Main function to run the test
#     """
#     print("=" * 80)
#     print("Learning to Rank System Test")
#     print("=" * 80)
    
#     start_time = datetime.now()
#     results = test_learning_to_rank()
#     end_time = datetime.now()
    
#     print("\n" + "=" * 80)
#     print("Test Summary:")
#     print(f"Total time: {end_time - start_time}")
#     print("=" * 80)
    
#     # Compare approaches
#     for approach, approach_results in results.items():
#         print(f"\n{approach.upper()} Approach Summary:")
#         print("-" * 40)
        
#         # Calculate average scores
#         avg_top_score = np.mean([r["top_5_scores"][0] for r in approach_results])
#         print(f"Average top score: {avg_top_score:.4f}")
        
#         if "precision_at_3" in approach_results[0]:
#             avg_precision = np.mean([r["precision_at_3"] for r in approach_results])
#             print(f"Average Precision@3: {avg_precision:.4f}")

# if __name__ == "__main__":
#     main()