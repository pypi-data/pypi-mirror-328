from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk import sent_tokenize, word_tokenize
import nltk
import json

@dataclass
class SRSWTIAspect:
    """Data class for aspect-based analysis"""
    text: str
    sentiment_score: float
    context: str
    position: Tuple[int, int]
    modifiers: List[str]

@dataclass
class SRSWTISentiment:
    """Data class for sentiment scores"""
    compound: float
    positive: float
    negative: float
    neutral: float

class SRSWTISentimentAnalyzer:
    """Advanced sentiment analysis with aspect-based capabilities"""
    
    def __init__(self, custom_domain_modifiers: Optional[Dict[str, Dict[str, float]]] = None):
        self.sia = SentimentIntensityAnalyzer()
        # Default domain modifiers
        self.domain_modifiers = {
            'product': {'great': 1.3, 'defective': -1.5},
            'service': {'quick': 1.2, 'slow': -1.2},
            'price': {'worth': 1.4, 'expensive': -1.1}
        }
        
        # Allow custom domain modifiers during initialization
        if custom_domain_modifiers:
            self.domain_modifiers.update(custom_domain_modifiers)
    
    def add_domain_modifier(self, domain: str, word: str, modifier: float):
        """
        Dynamically add a domain-specific sentiment modifier
        
        Args:
            domain: Domain to modify (e.g., 'restaurant')
            word: Word to modify sentiment for
            modifier: Sentiment multiplier
        """
        if domain not in self.domain_modifiers:
            self.domain_modifiers[domain] = {}
        
        self.domain_modifiers[domain][word] = modifier
        
    def analyze(self, 
                text: str, 
                aspects: Optional[List[str]] = None,
                domain: Optional[str] = None) -> Dict:
        """
        Perform comprehensive sentiment analysis
        
        Args:
            text: Input text
            aspects: List of aspects to analyze
            domain: Domain for specific sentiment modifications
            
        Returns:
            Dict containing detailed sentiment analysis
        """
        # Basic sentiment analysis
        sentences = sent_tokenize(text)
        overall_sentiment = self._get_sentiment(text)
        
        # Sentence-level analysis
        sentence_analysis = [
            {
                'text': sentence,
                'sentiment': self._get_sentiment(sentence),
                'intensifiers': self._find_intensifiers(sentence),
                'length': len(word_tokenize(sentence))
            }
            for sentence in sentences
        ]
        
        # Aspect-based analysis if aspects provided
        aspect_analysis = {}
        if aspects:
            aspect_analysis = self._analyze_aspects(text, aspects, domain)
        
        return {
            'overall': {
                'sentiment': overall_sentiment.__dict__,
                'text_stats': {
                    'sentence_count': len(sentences),
                    'word_count': len(word_tokenize(text)),
                    'avg_sentence_length': sum(s['length'] for s in sentence_analysis) / len(sentences)
                }
            },
            'sentences': sentence_analysis,
            'aspects': {
                aspect: {
                    'mentions': [mention.__dict__ for mention in mentions]
                }
                for aspect, mentions in aspect_analysis.items()
            } if aspects else {},
            'summary': self._generate_summary(overall_sentiment, aspect_analysis)
        }
    
    def _get_sentiment(self, text: str) -> SRSWTISentiment:
        """Get sentiment scores for text"""
        scores = self.sia.polarity_scores(text)
        return SRSWTISentiment(
            compound=scores['compound'],
            positive=scores['pos'],
            negative=scores['neg'],
            neutral=scores['neu']
        )
    
    def _find_intensifiers(self, text: str) -> List[Dict[str, str]]:
        """Find words that intensify sentiment"""
        tokens = word_tokenize(text)
        tagged = nltk.pos_tag(tokens)
        
        intensifiers = []
        for i, (word, tag) in enumerate(tagged):
            if tag in ['RB', 'RBR', 'RBS'] and i + 1 < len(tagged):
                intensifiers.append({
                    'intensifier': word,
                    'modified_word': tagged[i + 1][0]
                })
        
        return intensifiers
    
    def _analyze_aspects(self, 
                        text: str, 
                        aspects: List[str],
                        domain: Optional[str] = None) -> Dict[str, List[SRSWTIAspect]]:
        """Perform aspect-based sentiment analysis"""
        sentences = sent_tokenize(text)
        aspect_mentions = {aspect: [] for aspect in aspects}
        
        for sentence in sentences:
            for aspect in aspects:
                if aspect.lower() in sentence.lower():
                    # Get sentiment with domain-specific modifications
                    sentiment_score = self._get_domain_modified_sentiment(
                        sentence, domain) if domain else self._get_sentiment(sentence).compound
                    
                    # Find modifying words around aspect
                    tokens = word_tokenize(sentence)
                    aspect_idx = tokens.index(aspect)
                    context_window = 3
                    start_idx = max(0, aspect_idx - context_window)
                    end_idx = min(len(tokens), aspect_idx + context_window + 1)
                    
                    modifiers = self._extract_modifiers(tokens[start_idx:end_idx])
                    
                    aspect_mentions[aspect].append(
                        SRSWTIAspect(
                            text=aspect,
                            sentiment_score=sentiment_score,
                            context=sentence,
                            position=(start_idx, end_idx),
                            modifiers=modifiers
                        )
                    )
        
        return aspect_mentions
    
    def _get_domain_modified_sentiment(self, text: str, domain: str) -> float:
        """Apply domain-specific sentiment modifications"""
        base_sentiment = self._get_sentiment(text).compound
        
        if domain in self.domain_modifiers:
            words = word_tokenize(text.lower())
            modifiers = self.domain_modifiers[domain]
            
            for word in words:
                if word in modifiers:
                    base_sentiment *= modifiers[word]
        
        return max(min(base_sentiment, 1.0), -1.0)  # Clamp between -1 and 1
    
    def _extract_modifiers(self, tokens: List[str]) -> List[str]:
        """Extract words that modify an aspect"""
        tagged = nltk.pos_tag(tokens)
        return [word for word, tag in tagged if tag in ['JJ', 'JJR', 'JJS', 'RB', 'RBR', 'RBS']]
    
    def _generate_summary(self, 
                         overall_sentiment: SRSWTISentiment,
                         aspect_analysis: Dict) -> str:
        """Generate natural language summary of analysis"""
        sentiment_level = (
            'very positive' if overall_sentiment.compound > 0.5
            else 'positive' if overall_sentiment.compound > 0
            else 'very negative' if overall_sentiment.compound < -0.5
            else 'negative' if overall_sentiment.compound < 0
            else 'neutral'
        )
        
        summary = f"The overall sentiment is {sentiment_level}"
        
        if aspect_analysis:
            aspect_summaries = []
            for aspect, mentions in aspect_analysis.items():
                if mentions:
                    avg_sentiment = sum(m.sentiment_score for m in mentions) / len(mentions)
                    aspect_summaries.append(
                        f"{aspect} is mentioned {len(mentions)} times and is generally "
                        f"{'positive' if avg_sentiment > 0 else 'negative'}"
                    )
            
            if aspect_summaries:
                summary += ". " + ". ".join(aspect_summaries)
        
        return summary


def main():
    # Example of dynamic domain and aspect usage
    
    # Initialize with custom domain modifiers
    custom_modifiers = {
        'restaurant': {
            'delicious': 1.4,
            'expensive': -1.2,
            'crowded': -0.5
        }
    }
    analyzer = SRSWTISentimentAnalyzer(custom_domain_modifiers=custom_modifiers)
    
    # Dynamically add more modifiers
    analyzer.add_domain_modifier('restaurant', 'friendly', 1.3)
    
    # Expanded text with more emotional nuance and complexity
    text = "The restaurant was incredibly crowded and somewhat chaotic, which initially made me anxious. However, the food was surprisingly delicious and brought me pure joy. The staff's friendly demeanor and warm smiles quickly transformed my frustration into comfort and happiness."
    
    # More dynamic analysis with polar emotions and detailed context
    results = analyzer.analyze(
        text, 
        aspects=['food', 'staff', 'crowded', 'atmosphere', 'service'], 
        domain='restaurant'
    )
    
    print(json.dumps(results, indent=2, default=lambda obj: obj.__dict__ if hasattr(obj, '__dict__') else str(obj)))

if __name__ == "__main__":
    main()