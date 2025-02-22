from typing import Dict, List, Tuple, Optional, Union
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from datetime import datetime
import logging
import os
from pathlib import Path
import json
from dataclasses import dataclass

# Hide external library imports
import nltk as _nltk
from nltk import RegexpParser as _RegexpParser, Tree as _Tree
from nltk.chunk import ne_chunk as _ne_chunk
from nltk.sentiment import SentimentIntensityAnalyzer as _SentimentIntensityAnalyzer

# Set up logging
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)
log_file = log_dir / f"srswti_text_analyzer_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - SRSWTI - %(levelname)s - %(message)s'
)
logger = logging.getLogger("SRSWTI")

# Initialize console
console = Console()

# Download required resources silently
with Progress(
    SpinnerColumn(),
    TextColumn("[bold blue]Initializing SRSWTI Text Analysis Engine..."),
    transient=True,
) as progress:
    _nltk.download('vader_lexicon', quiet=True)
    _nltk.download('punkt', quiet=True)
    _nltk.download('averaged_perceptron_tagger', quiet=True)
    _nltk.download('maxent_ne_chunker', quiet=True)
    _nltk.download('words', quiet=True)
    logger.info("SRSWTI Text Analysis Engine initialized successfully")

@dataclass
class SRSWTIEntityInfo:
    """SRSWTI Entity Information Container"""
    text: str
    label: str
    confidence: float
    start: int
    end: int

@dataclass
class SRSWTISentenceInfo:
    """SRSWTI Sentence Analysis Container"""
    text: str
    sentiment_scores: Dict[str, float]
    entities: List[SRSWTIEntityInfo]
    structure: Dict[str, Union[str, List[str]]]

class SRSWTITextAnalyzer:
    """SRSWTI Advanced Text Analysis Engine"""
    
    def __init__(self):
        logger.info("Initializing SRSWTI Text Analyzer")
        self.grammar = r"""
            NP: {<DT|PP\$>?<JJ>*<NN|NNS>}   # Noun phrase
            VP: {<VB.*><NP|PP>}             # Verb phrase
            PP: {<IN><NP>}                  # Prepositional phrase
            ADJP: {<JJ.*>}                  # Adjective phrase
        """
        self.chunk_parser = _RegexpParser(self.grammar)
        self.sia = _SentimentIntensityAnalyzer()
        logger.info("SRSWTI Text Analyzer initialized with standard grammar patterns")
        
    def analyze_text(self, text: str) -> Dict:
        """
        SRSWTI Comprehensive Text Analysis
        
        Args:
            text: Input text to analyze
            
        Returns:
            Dict containing structured analysis results
        """
        logger.info("Starting SRSWTI text analysis")
        with Progress(
            SpinnerColumn(),
            TextColumn("[bold blue]Processing text analysis..."),
            transient=True,
        ) as progress:
            sentences = _nltk.sent_tokenize(text)
            sentence_analysis = []
            
            overall_entities = []
            overall_phrases = {
                'noun_phrases': [],
                'verb_phrases': [],
                'prep_phrases': []
            }
            
            for sentence in sentences:
                analysis = self._analyze_sentence(sentence)
                sentence_analysis.append(analysis)
                overall_entities.extend(analysis.entities)
                
                for phrase_type, phrases in analysis.structure.items():
                    if phrase_type in overall_phrases:
                        overall_phrases[phrase_type].extend(phrases)
            
            overall_sentiment = self._calculate_overall_sentiment(sentence_analysis)
            
            logger.info(f"Completed analysis of {len(sentences)} sentences")
            
            return {
                'summary': {
                    'text_length': len(text),
                    'sentence_count': len(sentences),
                    'overall_sentiment': overall_sentiment,
                    'entity_count': len(overall_entities),
                    'unique_entities': len(set(e.text for e in overall_entities))
                },
                'sentiment': {
                    'overall': overall_sentiment,
                    'by_sentence': [
                        {
                            'text': analysis.text,
                            'scores': analysis.sentiment_scores
                        }
                        for analysis in sentence_analysis
                    ]
                },
                'entities': [
                    {
                        'text': entity.text,
                        'label': entity.label,
                        'confidence': entity.confidence,
                        'position': {'start': entity.start, 'end': entity.end}
                    }
                    for entity in overall_entities
                ],
                'structure': {
                    'phrases': overall_phrases,
                    'by_sentence': [
                        {
                            'text': analysis.text,
                            'structure': analysis.structure
                        }
                        for analysis in sentence_analysis
                    ]
                }
            }
    
    def _analyze_sentence(self, sentence: str) -> SRSWTISentenceInfo:
        """SRSWTI Sentence Analysis"""
        tokens = _nltk.word_tokenize(sentence)
        tagged = _nltk.pos_tag(tokens)
        
        entities = self._extract_entities(tagged)
        tree = self.chunk_parser.parse(tagged)
        structure = self._extract_structure(tree)
        sentiment_scores = self.sia.polarity_scores(sentence)
        
        return SRSWTISentenceInfo(
            text=sentence,
            sentiment_scores=sentiment_scores,
            entities=entities,
            structure=structure
        )
    
    def _extract_entities(self, tagged_tokens: List[Tuple[str, str]]) -> List[SRSWTIEntityInfo]:
        """SRSWTI Entity Extraction"""
        ne_tree = _ne_chunk(tagged_tokens)
        entities = []
        
        for chunk in ne_tree:
            if isinstance(chunk, _Tree):
                text = ' '.join(token for token, tag in chunk.leaves())
                entities.append(SRSWTIEntityInfo(
                    text=text,
                    label=chunk.label(),
                    confidence=0.85,
                    start=0,
                    end=0
                ))
        
        return entities
    
    def _extract_structure(self, tree: _Tree) -> Dict[str, List[str]]:
        """SRSWTI Structure Analysis"""
        phrases = {
            'noun_phrases': [],
            'verb_phrases': [],
            'prep_phrases': [],
            'adj_phrases': []
        }
        
        for subtree in tree.subtrees():
            if subtree.label() in ['NP', 'VP', 'PP', 'ADJP']:
                phrase_text = ' '.join(word for word, tag in subtree.leaves())
                if subtree.label() == 'NP':
                    phrases['noun_phrases'].append(phrase_text)
                elif subtree.label() == 'VP':
                    phrases['verb_phrases'].append(phrase_text)
                elif subtree.label() == 'PP':
                    phrases['prep_phrases'].append(phrase_text)
                elif subtree.label() == 'ADJP':
                    phrases['adj_phrases'].append(phrase_text)
                    
        return phrases
    
    def _calculate_overall_sentiment(self, 
                                   sentence_analyses: List[SRSWTISentenceInfo]) -> Dict[str, float]:
        """SRSWTI Sentiment Calculation"""
        if not sentence_analyses:
            return {'compound': 0.0, 'pos': 0.0, 'neg': 0.0, 'neu': 0.0}
            
        sentiments = [analysis.sentiment_scores for analysis in sentence_analyses]
        return {
            'compound': sum(s['compound'] for s in sentiments) / len(sentiments),
            'pos': sum(s['pos'] for s in sentiments) / len(sentiments),
            'neg': sum(s['neg'] for s in sentiments) / len(sentiments),
            'neu': sum(s['neu'] for s in sentiments) / len(sentiments)
        }

def main():
    # Example usage
    analyzer = SRSWTITextAnalyzer()
    
    text = """
    Apple Inc. announced a new iPhone yesterday in Cupertino. 
    The device features an impressive camera system and powerful AI capabilities. 
    CEO Tim Cook called it "the best iPhone we've ever made."
    """
    
    results = analyzer.analyze_text(text)
    
    # Print formatted results
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()