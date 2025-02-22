# from typing import Dict, List, Optional
# import spacy
# import scispacy
# import fitz
# import logging
# import subprocess
# import sys
# from flair.data import Sentence
# from flair.models import SequenceTagger
# from scispacy.linking import EntityLinker
# from scispacy.abbreviation import AbbreviationDetector

# class SRSWTIScientificProcessor:
#     """SRSWTI Scientific Text Processing System"""
    
#     def __init__(self):
#         """Initialize the scientific text processor with required models and logging"""
#         # Configure logging
#         self.logger = logging.getLogger("SRSWTI-SciProcessor")
#         logging.basicConfig(
#             level=logging.INFO,
#             format='%(asctime)s [%(levelname)s] SRSWTI-SciProcessor: %(message)s',
#             datefmt='%Y-%m-%d %H:%M:%S'
#         )
        
#         # Download and initialize models
#         self._initialize_models()
        
#     def _initialize_models(self):
#         """Initialize all required NLP models and pipelines"""
#         try:
#             # Initialize main ScispaCy model
#             self.nlp_sci = spacy.load("en_core_sci_md")
#             self.logger.info("Loaded en_core_sci_md model")
            
#             # Add UMLS linker
#             self.nlp_sci.add_pipe("scispacy_linker", 
#                                 config={"resolve_abbreviations": True, 
#                                       "linker_name": "umls"})
#             self.logger.info("Added UMLS entity linker")
            
#             # Add abbreviation detector
#             self.nlp_sci.add_pipe("abbreviation_detector")
#             self.logger.info("Added abbreviation detector")
            
#             # Initialize Flair BioNER
#             self.bio_tagger = SequenceTagger.load('bioner')
#             self.logger.info("Loaded Flair BioNER tagger")
            
#         except Exception as e:
#             self.logger.error(f"Model initialization failed: {e}")
#             raise

#     def download_scispacy_model(self, model_name="en_core_sci_sm"):
#         """Download ScispaCy model if not already installed"""
#         try:
#             spacy.load(model_name)
#             self.logger.info(f"{model_name} model already installed")
#         except OSError:
#             self.logger.info(f"Downloading {model_name} model...")
#             subprocess.check_call([
#                 sys.executable, 
#                 "-m", 
#                 "pip", 
#                 "install", 
#                 f"https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.1/{model_name}-0.5.1.tar.gz"
#             ])
#             self.logger.info(f"Successfully downloaded {model_name}")

#     def process_paper(self, text: str) -> Dict:
#         """Process scientific text and extract various linguistic features"""
#         try:
#             # Process with ScispaCy
#             doc_sci = self.nlp_sci(text)
            
#             # Process with Flair
#             sentence = Sentence(text)
#             self.bio_tagger.predict(sentence)
            
#             results = {
#                 'entities': self._get_entities(doc_sci),
#                 'abbreviations': self._get_abbreviations(doc_sci),
#                 'bio_entities': self._get_bio_entities(sentence),
#                 'linked_concepts': self._get_linked_concepts(doc_sci)
#             }
            
#             self.logger.info(f"Successfully processed text of length {len(text)}")
#             return results
            
#         except Exception as e:
#             self.logger.error(f"Error processing text: {e}")
#             raise
    
#     def _get_entities(self, doc) -> List[Dict]:
#         """Extract named entities from processed document"""
#         return [{'text': ent.text, 
#                 'label': ent.label_, 
#                 'start': ent.start_char, 
#                 'end': ent.end_char}
#                 for ent in doc.ents]
    
#     def _get_abbreviations(self, doc) -> List[Dict]:
#         """Extract abbreviations and their definitions"""
#         abbrevs = []
#         for abrv in doc._.abbreviations:
#             abbrevs.append({
#                 'abbrev': abrv.text,
#                 'definition': abrv._.long_form.text
#             })
#         return abbrevs

#     def _get_bio_entities(self, sentence) -> List[Dict]:
#         """Extract biomedical entities using Flair"""
#         return [{'text': entity.text, 
#                 'label': entity.tag}
#                 for entity in sentence.get_spans('ner')]

#     def _get_linked_concepts(self, doc) -> List[Dict]:
#         """Extract UMLS-linked concepts"""
#         linked = []
#         for ent in doc.ents:
#             if ent._.kb_ids:
#                 linked.append({
#                     'text': ent.text,
#                     'umls_ids': ent._.kb_ids
#                 })
#         return linked

#     def run_test(self):
#         """Run a test of the processor with sample text"""
#         try:
#             sample_text = (
#                 "CRISPR-Cas9 is a revolutionary gene-editing technology. "
#                 "The protein Cas9 can precisely cut DNA at specific locations. "
#                 "This technique has significant implications for treating genetic disorders."
#             )
            
#             self.logger.info("Running test with sample text")
#             results = self.process_paper(sample_text)
            
#             print("\n=== ScispaCy Processor Test Results ===")
            
#             print("\n1. Named Entities:")
#             for entity in results['entities']:
#                 print(f"  - {entity['text']} (Type: {entity['label']})")
            
#             print("\n2. Abbreviations:")
#             for abbrev in results['abbreviations']:
#                 print(f"  - {abbrev['abbrev']}: {abbrev['definition']}")
            
#             print("\n3. Bio Entities:")
#             for bio_entity in results['bio_entities']:
#                 print(f"  - {bio_entity['text']} (Tag: {bio_entity['label']})")
            
#             print("\n4. Linked Concepts:")
#             for concept in results['linked_concepts']:
#                 print(f"  - {concept['text']} (UMLS IDs: {concept['umls_ids']})")
                
#             self.logger.info("Test completed successfully")
            
#         except Exception as e:
#             self.logger.error(f"Test failed: {e}")
#             raise

# if __name__ == "__main__":
#     processor = SRSWTIScientificProcessor()
#     processor.run_test()
