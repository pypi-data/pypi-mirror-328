
# import spacy
# from typing import List, Dict, Optional, Union
# def _check_spacy_model():
#     try:
#         import spacy
#     except ImportError:
#         print("Error: spaCy is not installed. Please install it first.")
#         return

#     try:
#         spacy.load('en_core_web_sm')
#     except OSError:
#         print("SpaCy model 'en_core_web_sm' not found. Downloading now...")
#         import subprocess
#         import sys
        
#         try:
#             subprocess.check_call([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])
#             print("Successfully downloaded 'en_core_web_sm' model.")
#         except subprocess.CalledProcessError:
#             print("Failed to download 'en_core_web_sm' model. Please check your internet connection and try manually.")
# _check_spacy_model()

# class SRSWTISpacyProcessor:
#     """Spacy-based text processing operations."""
    
#     def __init__(self, model: str = 'en_core_web_sm'):
#         """
#         Initialize Spacy processor.
        
#         Args:
#             model: Name of the Spacy model to use
#         """
#         self.nlp = spacy.load(model)
    
#     def process_text(self, text: str, features: Optional[List[str]] = None) -> Dict:
#         """
#         Process text through Spacy pipeline.
        
#         Args:
#             text: Input text
#             features: List of features to extract:
#                 - tokens: Token information
#                 - sentences: Sentence segmentation
#                 - lemmas: Lemmatization
#                 - pos: Part-of-speech tags
#                 - deps: Dependency parsing
#                 - ents: Named entities
#                 - noun_chunks: Noun phrases
#         """
#         if features is None:
#             features = ['tokens', 'sentences', 'lemmas', 'pos', 'deps', 'ents']
            
#         doc = self.nlp(text)
#         result = {}
        
#         for feature in features:
#             if feature == 'tokens':
#                 result['tokens'] = [token.text for token in doc]
#             elif feature == 'sentences':
#                 result['sentences'] = [sent.text for sent in doc.sents]
#             elif feature == 'lemmas':
#                 result['lemmas'] = [token.lemma_ for token in doc]
#             elif feature == 'pos':
#                 result['pos_tags'] = [(token.text, token.pos_) for token in doc]
#             elif feature == 'deps':
#                 result['dependencies'] = [(token.text, token.dep_, token.head.text) 
#                                         for token in doc]
#             elif feature == 'ents':
#                 result['entities'] = [(ent.text, ent.label_) for ent in doc.ents]
#             elif feature == 'noun_chunks':
#                 result['noun_phrases'] = [chunk.text for chunk in doc.noun_chunks]
                
#         return result
    
#     def get_similarity(self, text1: str, text2: str) -> float:
#         """Calculate semantic similarity between two texts."""
#         doc1 = self.nlp(text1)
#         doc2 = self.nlp(text2)
#         return doc1.similarity(doc2)
    
#     def get_vector(self, text: str) -> List[float]:
#         """Get vector representation of text."""
#         doc = self.nlp(text)
#         return doc.vector.tolist()
    
#     def extract_keywords(self, text: str, n_keywords: int = 10) -> List[str]:
#         """Extract important keywords from text."""
#         doc = self.nlp(text)
#         keywords = []
        
#         # Filter for nouns and proper nouns
#         for token in doc:
#             if token.pos_ in ['NOUN', 'PROPN'] and not token.is_stop:
#                 keywords.append(token.text)
                
#         # Sort by frequency and return top n
#         from collections import Counter
#         return [word for word, _ in Counter(keywords).most_common(n_keywords)]
    


# # def main():
# #     # Initialize the processor
# #     processor = SRSWTISpacyProcessor()
    
# #     # Sample text for testing
# #     sample_text = "Apple Inc. is a leading technology company based in Cupertino, California."
    
# #     # Test process_text with all features
# #     print("### Processing Text ###")
# #     processed_text = processor.process_text(sample_text)
# #     for feature, value in processed_text.items():
# #         print(f"{feature.capitalize()}: {value}")
    
# #     # Test process_text with specific features
# #     print("\n### Processing Text with Specific Features ###")
# #     specific_features = processor.process_text(sample_text, features=['ents', 'noun_chunks'])
# #     for feature, value in specific_features.items():
# #         print(f"{feature.capitalize()}: {value}")
    
# #     # Test similarity
# #     print("\n### Semantic Similarity ###")
# #     text1 = "The cat sits on the mat"
# #     text2 = "A feline is resting on the carpet"
# #     similarity = processor.get_similarity(text1, text2)
# #     print(f"Similarity between '{text1}' and '{text2}': {similarity}")
    
# #     # Test vector representation
# #     print("\n### Text Vector ###")
# #     vector = processor.get_vector(sample_text)
# #     print(f"Vector length: {len(vector)}")
# #     print(f"First 5 vector elements: {vector[:5]}")
    
# #     # Test keyword extraction
# #     print("\n### Keyword Extraction ###")
# #     keywords = processor.extract_keywords(sample_text)
# #     print(f"Keywords: {keywords}")

# # if __name__ == "__main__":
# #     main()