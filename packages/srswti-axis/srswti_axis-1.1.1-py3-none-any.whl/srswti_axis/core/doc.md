# srswti text cleaner

clean text intelligently. boost llm inputs. handle messy data.

## quick start

```python
from srswti_axis import SRSWTITextCleaner

cleaner = SRSWTITextCleaner()
clean_text = cleaner.clean_text("Here's some messy text! http://example.com")
```

## core features

- 🧹 smart html cleanup
- 🔗 url handling
- 📧 email management
- 🔤 unicode normalization
- 💬 contraction handling
- 🔢 number standardization
- ⚡ special char processing
- 📝 whitespace optimization

## real-world examples

### llm input preprocessing

```python
# prepare text for llm api calls
def prepare_for_llm(text: str) -> str:
    cleaner = SRSWTITextCleaner()
    
    # custom options for llm input
    options = {
        'remove_html': True,
        'remove_urls': False,  # keep urls for context
        'normalize_unicode': True,
        'expand_contractions': True,
        'normalize_numbers': False,  # keep numbers
        'remove_special': False,  # keep punctuation
        'normalize_whitespace': True
    }
    
    return cleaner.clean_text(text, options)

# example usage
messy_prompt = """
<div>User query about product #123</div>
They're asking about https://example.com/product
Price: $299.99 • Rating: ★★★★☆
"""

clean_prompt = prepare_for_llm(messy_prompt)
# result: "User query about product 123 They are asking about 
#         https://example.com/product Price: $299.99 Rating: ****"
```

### data cleaning pipeline

```python
def clean_customer_feedback(feedback: str) -> str:
    cleaner = SRSWTITextCleaner()
    
    # step 1: basic cleaning
    text = cleaner.remove_html(feedback)
    text = cleaner.remove_emails(text)
    
    # step 2: normalization
    text = cleaner.normalize_unicode(text)
    text = cleaner.expand_contractions(text)
    
    # step 3: final touchup
    text = cleaner.normalize_whitespace(text)
    
    return text

# example
feedback = """
<p>Customer feedback:</p>
I'm not happy with product #123!!! 
Contact: angry@customer.com
Rating: ★☆☆☆☆
"""
```

### web scraping cleanup

```python
def clean_scraped_content(html_content: str) -> str:
    cleaner = SRSWTITextCleaner()
    options = {
        'remove_html': True,
        'remove_urls': True,
        'normalize_unicode': True,
        'expand_contractions': True,
        'normalize_whitespace': True
    }
    return cleaner.clean_text(html_content, options)

# example
scraped = """
<article>
    <h1>Top 10 AI Trends</h1>
    <p>Visit our blog at https://blog.example.com</p>
    <p>We're seeing amazing advances in AI!</p>
</article>
"""
```

### social media preprocessing

```python
def normalize_social_post(post: str) -> str:
    cleaner = SRSWTITextCleaner()
    options = {
        'normalize_unicode': True,
        'expand_contractions': True,
        'remove_urls': False,
        'normalize_whitespace': True
    }
    return cleaner.clean_text(post, options)

# example
tweet = """
OMG!!! 🔥 This product is amazing!!!
Check it out: https://example.com
I can't believe it's only $99.99!!!
"""
```

## advanced use cases

### llm chain preprocessing

```python
# prepare text for different llm chain stages
def prepare_chain_input(text: str, stage: str) -> str:
    cleaner = SRSWTITextCleaner()
    
    options = {
        'classification': {
            'remove_html': True,
            'normalize_unicode': True,
            'expand_contractions': True,
            'normalize_numbers': True,
            'normalize_whitespace': True
        },
        'summarization': {
            'remove_html': True,
            'remove_urls': True,
            'normalize_unicode': True,
            'expand_contractions': False,
            'normalize_whitespace': True
        },
        'sentiment': {
            'remove_html': True,
            'normalize_unicode': True,
            'expand_contractions': True,
            'remove_special': False,
            'normalize_whitespace': True
        }
    }
    
    return cleaner.clean_text(text, options.get(stage, {}))
```

### document preprocessing

```python
def prepare_document(doc: str) -> str:
    cleaner = SRSWTITextCleaner()
    
    # step 1: structural cleaning
    doc = cleaner.remove_html(doc)
    doc = cleaner.normalize_whitespace(doc)
    
    # step 2: content normalization
    doc = cleaner.normalize_unicode(doc)
    doc = cleaner.expand_contractions(doc)
    
    # step 3: special handling
    doc = cleaner.remove_special_characters(
        doc,
        keep_chars=".,!?-"  # keep basic punctuation
    )
    
    return doc
```

## performance tips

### batch processing

```python
def clean_batch(texts: list) -> list:
    cleaner = SRSWTITextCleaner()
    return [cleaner.clean_text(text) for text in texts]

# example
batch = [
    "<p>First text</p>",
    "Second text with https://example.com",
    "Third text with special chars #@$%"
]
clean_batch(batch)
```

### memory optimization

```python
def clean_large_text(text: str) -> str:
    cleaner = SRSWTITextCleaner()
    
    # process in chunks
    chunk_size = 1000000  # 1MB chunks
    chunks = [text[i:i+chunk_size] 
             for i in range(0, len(text), chunk_size)]
    
    return " ".join(
        cleaner.clean_text(chunk) 
        for chunk in chunks
    )
```

## typical workflows

### data science pipeline
```python
def preprocess_dataset(texts: list) -> list:
    cleaner = SRSWTITextCleaner()
    options = {
        'remove_html': True,
        'normalize_unicode': True,
        'expand_contractions': True,
        'normalize_numbers': True,
        'normalize_whitespace': True
    }
    return [cleaner.clean_text(text, options) for text in texts]
```

### chatbot preprocessing
```python
def prepare_chat_input(user_input: str) -> str:
    cleaner = SRSWTITextCleaner()
    options = {
        'normalize_unicode': True,
        'expand_contractions': True,
        'normalize_whitespace': True,
        'remove_special': False  # keep emotion indicators
    }
    return cleaner.clean_text(user_input, options)
```

## coming soon

- custom regex patterns
- language-specific cleaning
- smart entity recognition
- batch processing
- async support
- pipeline integration
- llm-specific presets

that's it. clean text, happy llms.


# srswti text analyzer

intelligent text analysis with progress tracking, pure NLP--NOTHING ELSE.

## quick start

```python
from srswti_axis import SRSWTITextAnalyzer

analyzer = SRSWTITextAnalyzer()
text = "Apple Inc. announced a new iPhone yesterday. CEO Tim Cook was excited."
results = analyzer.analyze_text(text)
```

## key features

- ner with confidence scores
- deep structural analysis

- advanced sentiment scoring
- comprehensive phrase extraction
- automatic resource management
- super fast, like 20 ms

## analysis components

### initialization
```python
# automatic resource download with progress
analyzer = SRSWTITextAnalyzer()
# logs/srswti_text_analyzer_20250213_123456.log created
# nltk resources downloaded silently
```

### core analysis
```python
# analyze with progress tracking
results = analyzer.analyze_text(
    "Google announced new AI features. Users are excited."
)

# returns structured dict with:
{
    'summary': {
        'text_length': 52,
        'sentence_count': 2,
        'overall_sentiment': {'compound': 0.8, 'pos': 0.6, 'neg': 0.0, 'neu': 0.4},
        'entity_count': 2,
        'unique_entities': 2
    },
    'sentiment': {
        'overall': {'compound': 0.8, 'pos': 0.6, 'neg': 0.0, 'neu': 0.4},
        'by_sentence': [
            {'text': 'Google announced new AI features.', 'scores': {'compound': 0.3}},
            {'text': 'Users are excited.', 'scores': {'compound': 0.7}}
        ]
    },
    'entities': [
        {'text': 'Google', 'label': 'ORG', 'confidence': 0.98},
        {'text': 'AI', 'label': 'PRODUCT', 'confidence': 0.85}
    ],
    'structure': {
        'phrases': {
            'noun_phrases': ['Google', 'AI features', 'Users'],
            'verb_phrases': ['announced', 'are excited']
        },
        'by_sentence': [
            {'text': 'Google announced new AI features.', 'phrases': 2},
            {'text': 'Users are excited.', 'phrases': 1}
        ]
    }
}

## real-world applications

### product review analysis
```python
def analyze_reviews(reviews: list) -> dict:
    analyzer = SRSWTITextAnalyzer()
    results = {}
    
    for review in reviews:
        analysis = analyzer.analyze_text(review)
        results[review] = {
            'sentiment': analysis['sentiment']['overall'],
            'features_mentioned': analysis['structure']['phrases']['noun_phrases'],
            'key_entities': [e['text'] for e in analysis['entities']],
            'highlights': [
                s['text'] for s in analysis['sentiment']['by_sentence']
                if s['scores']['compound'] > 0.5
            ]
        }
    
    return results
```

### news content analysis
```python
def analyze_article(article: str) -> dict:
    analyzer = SRSWTITextAnalyzer()
    
    # full analysis with progress tracking
    analysis = analyzer.analyze_text(article)
    
    return {
        'key_points': {
            'organizations': [
                e['text'] for e in analysis['entities']
                if e['label'] == 'ORGANIZATION'
            ],
            'people': [
                e['text'] for e in analysis['entities']
                if e['label'] == 'PERSON'
            ],
            'locations': [
                e['text'] for e in analysis['entities']
                if e['label'] == 'GPE'
            ]
        },
        'sentiment_flow': [
            {
                'text': s['text'],
                'sentiment': s['scores']
            }
            for s in analysis['sentiment']['by_sentence']
        ],
        'key_phrases': analysis['structure']['phrases']
    }
```

### advanced pattern analysis
```python
def extract_patterns(text: str) -> dict:
    analyzer = SRSWTITextAnalyzer()
    analysis = analyzer.analyze_text(text)
    
    return {
        'action_patterns': [
            {
                'subject': np,
                'action': vp
            }
            for np in analysis['structure']['phrases']['noun_phrases']
            for vp in analysis['structure']['phrases']['verb_phrases']
        ],
        'entity_relations': [
            {
                'entity': entity['text'],
                'context': [
                    s['text'] 
                    for s in analysis['sentiment']['by_sentence']
                    if entity['text'] in s['text']
                ]
            }
            for entity in analysis['entities']
        ]
    }
```

## data structures

### entity info
```python
@dataclass
class SRSWTIEntityInfo:
    text: str          # extracted text
    label: str         # entity type
    confidence: float  # confidence score
    start: int         # start position
    end: int          # end position
```

### sentence info
```python
@dataclass
class SRSWTISentenceInfo:
    text: str                      # sentence text
    sentiment_scores: Dict         # sentiment details
    entities: List[SRSWTIEntityInfo]  # found entities
    structure: Dict                # phrase analysis
```

## logging and tracking

### log structure
```
logs/
└── srswti_text_analyzer_20250213_123456.log


## performance tips

### memory management
```python
def process_large_text(text: str, chunk_size: int = 5000) -> dict:
    analyzer = SRSWTITextAnalyzer()
    chunks = [
        text[i:i+chunk_size] 
        for i in range(0, len(text), chunk_size)
    ]
    
    results = []
    for chunk in chunks:
        results.append(analyzer.analyze_text(chunk))
    
    # merge results...
```


## grammar patterns

built-in patterns:
```python
grammar = r"""
    NP: {<DT|PP\$>?<JJ>*<NN|NNS>}   # noun phrase
    VP: {<VB.*><NP|PP>}             # verb phrase
    PP: {<IN><NP>}                  # prep phrase
    ADJP: {<JJ.*>}                  # adj phrase
"""
```


## coming soon

- custom grammar patterns
- custom entity types
- export formats
- batch analysis
- streaming support

that's it. analyze with confidence.