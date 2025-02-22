# srswti sentiment analyzer

aspect-based sentiment analysis with domain-specific modifiers.

## quick start

```python
from srswti_axis import SRSWTISentimentAnalyzer

analyzer = SRSWTISentimentAnalyzer()

results = analyzer.analyze(
    text="The food was delicious but service was slow",
    aspects=['food', 'service'],
    domain='restaurant'
)
```

## core features

### basic analysis
```python
results = analyzer.analyze(text="sample text")

# returns:
{
    'overall': {
        'sentiment': {
            'compound': 0.5,    # overall score
            'positive': 0.6,    # positive ratio
            'negative': 0.1,    # negative ratio
            'neutral': 0.3     # neutral ratio
        },
        'text_stats': {
            'sentence_count': 2,
            'word_count': 10,
            'avg_sentence_length': 5.0
        }
    },
    'sentences': [...],
    'aspects': {},
    'summary': "The overall sentiment is positive"
}
```

### aspect-based analysis
```python
results = analyzer.analyze(
    text="The food was delicious",
    aspects=['food', 'service']
)

# returns additional aspect data:
{
    'aspects': {
        'food': {
            'mentions': [
                {
                    'text': 'food',
                    'sentiment_score': 0.8,
                    'context': 'The food was delicious',
                    'position': [1, 4],
                    'modifiers': ['delicious']
                }
            ]
        },
        'service': {
            'mentions': []
        }
    }
}
```

## domain customization

### custom modifiers
```python
# initialize with custom domains
analyzer = SRSWTISentimentAnalyzer(
    custom_domain_modifiers={
        'restaurant': {
            'delicious': 1.4,
            'expensive': -1.2,
            'crowded': -0.5
        }
    }
)

# add new modifiers
analyzer.add_domain_modifier(
    domain='restaurant',
    word='friendly',
    modifier=1.3
)
```

### default domains
```python
# built-in domains:
{
    'product': {
        'great': 1.3,
        'defective': -1.5
    },
    'service': {
        'quick': 1.2,
        'slow': -1.2
    },
    'price': {
        'worth': 1.4,
        'expensive': -1.1
    }
}
```

## output components

### sentiment scores
```python
@dataclass
class SRSWTISentiment:
    compound: float   # overall (-1 to 1)
    positive: float  # positive ratio
    negative: float  # negative ratio
    neutral: float   # neutral ratio
```

### aspect details
```python
@dataclass
class SRSWTIAspect:
    text: str            # aspect term
    sentiment_score: float  # sentiment
    context: str         # surrounding text
    position: Tuple[int, int]  # location
    modifiers: List[str]  # modifying words
```

## advanced usage

### detailed analysis
```python
results = analyzer.analyze(
    text="long review text...",
    aspects=['food', 'service', 'atmosphere'],
    domain='restaurant'
)

# extract specific aspects
food_mentions = results['aspects']['food']['mentions']
service_score = results['aspects']['service']['mentions'][0].sentiment_score

# get overall stats
sentence_count = results['overall']['text_stats']['sentence_count']
avg_length = results['overall']['text_stats']['avg_sentence_length']
```

### sentiment summary
```python
text = """
The restaurant was incredibly crowded but the 
food was delicious. Service was excellent.
"""

results = analyzer.analyze(
    text=text,
    aspects=['food', 'service', 'crowd'],
    domain='restaurant'
)

# gets natural language summary:
# "The overall sentiment is positive. 
#  food is mentioned 1 times and is generally positive. 
#  service is mentioned 1 times and is generally positive."
```

## interpretation guide

sentiment scores:
- -1.0 to -0.5: very negative
- -0.5 to 0.0: negative
- 0.0: neutral
- 0.0 to 0.5: positive
- 0.5 to 1.0: very positive

modifiers:
- > 1.0: amplifies positive
- < 1.0: amplifies negative
- 1.0: neutral effect

aspect coverage:
- mentioned: aspect found in text
- not mentioned: empty list
- sentiment: per-mention scoring

tbh we tried our best with pure nlp implementation for sentiment analsysis