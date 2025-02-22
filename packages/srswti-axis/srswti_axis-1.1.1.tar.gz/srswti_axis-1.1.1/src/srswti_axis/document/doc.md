# srswti document processing

document clustering and deduplication using wordllama.

## clusterer

clusters similar documents using kmeans algorithm.

```python
from srswti_axis import SrswtiClusterer

clusterer = SrswtiClusterer()
documents = [
    "first document about ai",
    "second document about ml",
    "third document about nlp"
]

# basic clustering
labels, inertia = clusterer.cluster_documents(documents, k=2)

# advanced clustering
labels, inertia = clusterer.cluster_documents(
    documents,
    k=3,                   # number of clusters
    max_iterations=100,    # max iterations
    tolerance=1e-4,        # convergence tolerance
    n_init=3              # number of initializations
)
```

### clustering applications

```python
# document organization
def organize_documents(docs: list, num_clusters: int) -> dict:
    clusterer = SrswtiClusterer()
    labels, _ = clusterer.cluster_documents(docs, k=num_clusters)
    
    clusters = {}
    for doc, label in zip(docs, labels):
        if label not in clusters:
            clusters[label] = []
        clusters[label].append(doc)
    
    return clusters

# topic grouping
def group_by_topics(articles: list) -> dict:
    clusterer = SrswtiClusterer()
    labels, _ = clusterer.cluster_documents(
        articles,
        k=5,
        max_iterations=200
    )
    return dict(zip(labels, articles))
```

## deduplicator

removes near-duplicate documents from collections.

```python
from srswti_axis import SrswtiDeduplicator

deduplicator = SrswtiDeduplicator()
documents = [
    "similar document about ai",
    "similar document about ai",
    "different document about ml"
]

# basic deduplication
unique_docs = deduplicator.deduplicate(documents)

# advanced deduplication
docs, indices = deduplicator.deduplicate(
    documents,
    threshold=0.5,        # similarity threshold
    return_indices=True   # return original indices
)
```

### deduplication applications

```python
# content cleaning
def clean_content(articles: list) -> list:
    deduplicator = SrswtiDeduplicator()
    return deduplicator.deduplicate(
        articles,
        threshold=0.7
    )

# find unique documents
def get_unique_with_sources(docs: list) -> dict:
    deduplicator = SrswtiDeduplicator()
    unique, indices = deduplicator.deduplicate(
        docs,
        threshold=0.8,
        return_indices=True
    )
    return {
        'unique_docs': unique,
        'original_indices': indices
    }
```

## advanced usage

### combined processing
```python
def process_document_collection(docs: list) -> dict:
    # first deduplicate
    deduplicator = SrswtiDeduplicator()
    unique_docs = deduplicator.deduplicate(docs, threshold=0.6)
    
    # then cluster
    clusterer = SrswtiClusterer()
    labels, _ = clusterer.cluster_documents(
        unique_docs,
        k=5,
        max_iterations=150
    )
    
    return {
        'unique_count': len(unique_docs),
        'clusters': labels
    }
```

### batch processing
```python
def batch_deduplicate(batches: list) -> list:
    deduplicator = SrswtiDeduplicator()
    results = []
    
    for batch in batches:
        unique = deduplicator.deduplicate(
            batch,
            threshold=0.5
        )
        results.extend(unique)
    
    return results
```

## usage notes

clustering:
- adjust k based on expected topics
- increase max_iterations for complex documents
- lower tolerance for higher precision
- increase n_init for better cluster stability

deduplication:
- higher threshold = stricter matching
- lower threshold = more duplicates removed
- return_indices helpful for tracking originals



# srswti graph merger

smart document merging with progress tracking.

## quick start

```python
from srswti_axis import SRSWTIGraphFlow

merger = SRSWTIGraphFlow()

documents = [
    "first document about ai",
    "second related document",
    "third overlapping content"
]

merged = merger.merge_documents(documents)
```

## basic usage

### initialize merger
```python
# default setup
merger = SRSWTIGraphFlow()

# custom setup
merger = SRSWTIGraphFlow(
    embedding_model='all-MiniLM-L6-v2',
    spacy_model='en_core_web_sm'
)
```

### merge documents
```python
# simple merge
merged = merger.merge_documents(documents)

# merge with automatic topic grouping
merged = merger.merge_documents(
    documents,  # list of documents
)
```

## progress tracking

the system shows real-time progress for:
```python
# visual progress bars for:
1. document processing
2. similarity analysis
3. merging operations
4. completion status
```

## logging

automatic logging to:
```
logs/
└── srswti_graph_merge.log

# tracks:
- processing steps
- completion status
- any errors
```

## working with large documents

```python
# process document batches
def process_large_collection(documents):
    merger = SRSWTIGraphFlow()
    
    # automatically handles:
    # - memory management
    # - progress tracking
    # - error recovery
    
    return merger.merge_documents(documents)
```

## common use cases

- merge similar documents
- combine related content
- remove redundant information
- organize by topics
- preserve important information
- maintain content flow

# srswti merger

intelligent document merging with multiple strategies.

## quick start

```python
from srswti_axis import SRSWTIPureFlow

merger = SRSWTIPureFlow()

# merge documents
documents = [
    "first document about ai",
    "second related document",
    "third document with overlap"
]

merged = merger.process(documents, method='similarity')
```

## initialization

```python
# default setup
merger = SRSWTIPureFlow()

# custom setup
merger = SRSWTIPureFlow(
    embedding_model='all-MiniLM-L6-v2',  # custom model
    language='en',                        # language
    spacy_model='en_core_web_sm'         # linguistic model
)
```

## merge methods

### similarity-based
```python
merged = merger.process(
    documents,
    method='similarity',
    threshold=0.5,                # similarity threshold
    strategy='clustering',        # merge strategy
    min_cluster_size=2,          # minimum cluster size
    adaptive_threshold=True       # auto-adjust threshold
)
```

### sequential
```python
merged = merger.process(
    documents,
    method='sequential',
    max_chunk_size=1000,         # max size per chunk
    overlap=True                 # maintain overlap
)
```

### graph-based
```python
merged = merger.process(
    documents,
    method='graph',
    threshold=0.7,               # similarity threshold
    merge_communities=True,      # use communities
    min_community_size=2,        # min community size
    edge_weight_method='combined' # weight calculation
)
```

### topic-based
```python
merged = merger.process(
    documents,
    method='topic',
    num_topics=5                # number of topics
)
```

## advanced usage

### batch processing
```python
def process_batch(documents, batch_size=10):
    merger = SRSWTIPureFlow()
    
    batches = [
        documents[i:i + batch_size]
        for i in range(0, len(documents), batch_size)
    ]
    
    results = []
    for batch in batches:
        merged = merger.process(batch, method='similarity')
        results.extend(merged)
    
    return results
```

### multi-method merging
```python
def merge_with_multiple_methods(documents):
    merger = SRSWTIPureFlow()
    
    # first by topic
    topic_merged = merger.process(
        documents,
        method='topic',
        num_topics=3
    )
    
    # then by similarity within topics
    final_merged = []
    for topic_docs in topic_merged.values():
        merged = merger.process(
            [topic_docs],
            method='similarity'
        )
        final_merged.extend(merged)
    
    return final_merged
```

### customized merging
```python
def merge_with_config(documents, config):
    merger = SRSWTIPureFlow(
        embedding_model=config.get('model'),
        language=config.get('language', 'en')
    )
    
    return merger.process(
        documents,
        method=config.get('method', 'similarity'),
        threshold=config.get('threshold', 0.5),
        min_cluster_size=config.get('min_size', 2)
    )
```

## method details

similarity-based:
- clusters similar documents
- adapts to content similarity
- maintains document coherence

sequential:
- preserves document order
- handles large documents
- optional content overlap

graph-based:
- finds document communities
- considers multiple similarities
- optimizes connections

topic-based:
- groups by content topics
- preserves topic coherence
- returns topic-organized results

# srswti divergence analyzer

semantic difference analysis between texts.

## quick start

```python
from srswti_axis import SRSWTIDivergence

analyzer = SRSWTIDivergence()

text1 = "cats are adorable pets"
text2 = "dogs are loyal companions"

# get basic divergence score
score = analyzer.calculate_divergence(text1, text2)

# get detailed analysis
details = analyzer.calculate_divergence(text1, text2, return_components=True)
```

## initialization

```python
# default setup
analyzer = SRSWTIDivergence()

# custom setup
analyzer = SRSWTIDivergence(
    embedding_model='all-MiniLM-L6-v2',    # model name
    semantic_dims=128,                      # dimensions
    semantic_temperature=0.1,               # distribution control
    projection_seed=42                      # reproducibility
)
```

## core methods

### calculate divergence
```python
# basic score
score = analyzer.calculate_divergence(text1, text2)

# detailed analysis
components = analyzer.calculate_divergence(
    text1,
    text2,
    return_components=True  # returns detailed metrics
)

# component details:
{
    'divergence_score': float,      # overall difference
    'cosine_similarity': float,     # vector similarity
    'jensen_shannon_divergence': float,  # distribution difference
    'entropy_p': float,             # first text complexity
    'entropy_q': float,             # second text complexity
    'text_complexity_1': float,     # first text score
    'text_complexity_2': float,     # second text score
    'cosine_weight': float,         # similarity weight
    'jsd_weight': float            # divergence weight
}
```

### compare texts
```python
results = analyzer.compare_texts(
    texts=[text1, text2, text3],
    reference_text=reference,    # optional
    threshold=0.5               # similarity threshold
)

# returns:
{
    'scores': [float],          # divergence scores
    'similar_texts': [str],     # texts below threshold
    'divergent_texts': [str]    # texts above threshold
}
```

### process documents
```python
results = analyzer.process(
    documents=[doc1, doc2, doc3],
    reference_doc=reference,    # optional
    threshold=0.5              # similarity threshold
)
```

## advanced usage

### batch analysis
```python
def analyze_batch(texts, ref_text):
    analyzer = SRSWTIDivergence()
    
    results = {
        'similar': [],
        'different': [],
        'scores': []
    }
    
    for text in texts:
        score = analyzer.calculate_divergence(
            ref_text,
            text,
            return_components=True
        )
        
        results['scores'].append(score)
        if score['divergence_score'] < 0.5:
            results['similar'].append(text)
        else:
            results['different'].append(text)
    
    return results
```

### detailed analysis
```python
def analyze_text_pair(text1, text2):
    analyzer = SRSWTIDivergence()
    
    components = analyzer.calculate_divergence(
        text1,
        text2,
        return_components=True
    )
    
    analysis = {
        'overall_difference': components['divergence_score'],
        'similarity': 1 - components['cosine_similarity'],
        'complexity_diff': abs(
            components['text_complexity_1'] - 
            components['text_complexity_2']
        ),
        'semantic_distance': components['jensen_shannon_divergence']
    }
    
    return analysis
```

### similarity grouping
```python
def group_by_similarity(texts, threshold=0.3):
    analyzer = SRSWTIDivergence()
    groups = []
    
    for text in texts:
        added = False
        for group in groups:
            score = analyzer.calculate_divergence(
                group[0],
                text
            )
            if score < threshold:
                group.append(text)
                added = True
                break
        
        if not added:
            groups.append([text])
    
    return groups
```

## interpretation guide

divergence scores:
- 0.0 - 0.3: very similar
- 0.3 - 0.5: moderately similar
- 0.5 - 0.7: moderately different
- 0.7 - 1.0: very different

component weights:
- cosine_weight: direct similarity
- jsd_weight: semantic distribution

complexity scores:
- closer to 0: simple text
- closer to 1: complex text

# srswti divergence v2

advanced semantic and topic-based text analysis.

## quick start

```python
from srswti_axis import SRSWTIDivergenceV2

analyzer = SRSWTIDivergenceV2()

text1 = "quantum computing enables parallel computation"
text2 = "classical computers use binary operations"

# basic divergence score
score = analyzer.calculate_divergence(text1, text2)

# detailed analysis
details = analyzer.calculate_divergence(text1, text2, return_components=True)
```

## initialization

```python
analyzer = SRSWTIDivergenceV2(
    embedding_model='all-MiniLM-L6-v2',    # model name
    semantic_dims=128,                      # semantic dimensions
    semantic_temperature=0.1,               # distribution control
    n_topics=10,                           # number of topics
    min_df=2                               # min document frequency
)
```

## core methods

### calculate divergence
```python
score = analyzer.calculate_divergence(text1, text2)

# detailed analysis
analysis = analyzer.calculate_divergence(
    text1,
    text2,
    return_components=True  # get detailed metrics
)

# returned components:
{
    'divergence_score': float,     # overall score
    'cosine_similarity': float,    # direct similarity
    'semantic_jsd': float,         # semantic difference
    'topic_jsd': float,           # topic difference
    'entropy_p': float,           # first text entropy
    'entropy_q': float,           # second text entropy
    'text_complexity_1': float,   # first text complexity
    'text_complexity_2': float,   # second text complexity
    'semantic_weight': float,     # semantic importance
    'topic_weight': float         # topic importance
}
```

### process documents
```python
results = analyzer.process(
    documents=[doc1, doc2, doc3],
    reference_doc=reference,   # optional
    threshold=0.5             # similarity threshold
)

# returns:
{
    'scores': [float],         # divergence scores
    'similar_texts': [str],    # similar documents
    'divergent_texts': [str]   # different documents
}
```

### topic analysis
```python
# get topic words
topics = analyzer.get_topic_words(top_n=10)

# returns list of word lists:
[
    ['quantum', 'computing', 'qubits'],
    ['neural', 'network', 'learning'],
    ...
]
```

## advanced usage

### combined topic and semantic analysis
```python
def analyze_document_similarity(doc1, doc2):
    analyzer = SRSWTIDivergenceV2(
        n_topics=5,
        semantic_dims=128
    )
    
    components = analyzer.calculate_divergence(
        doc1,
        doc2,
        return_components=True
    )
    
    analysis = {
        'overall_difference': components['divergence_score'],
        'semantic_similarity': 1 - components['semantic_jsd'],
        'topic_similarity': 1 - components['topic_jsd'],
        'complexity_comparison': abs(
            components['text_complexity_1'] - 
            components['text_complexity_2']
        )
    }
    
    return analysis
```

### document collection analysis
```python
def analyze_collection(documents):
    analyzer = SRSWTIDivergenceV2()
    
    # first get topics
    analyzer.process(documents)
    topics = analyzer.get_topic_words()
    
    # then analyze divergence
    reference = documents[0]
    results = analyzer.process(
        documents,
        reference_doc=reference
    )
    
    return {
        'topics': topics,
        'similar': results['similar_texts'],
        'different': results['divergent_texts']
    }
```

## score interpretation

divergence scores:
- 0.0 - 0.2: nearly identical
- 0.2 - 0.4: very similar
- 0.4 - 0.6: moderately different
- 0.6 - 0.8: substantially different
- 0.8 - 1.0: completely different

component weights:
- semantic_weight: meaning similarity
- topic_weight: subject matter similarity

complexity scores:
- 0.0 - 0.3: simple text
- 0.3 - 0.7: moderate complexity
- 0.7 - 1.0: high complexity

eveyrthing same except 10x better divergence calc for v2.


# srswti chunk analyzer

## overview
linguistic text analysis tool for advanced chunk extraction and parsing

## key features
- sentence tokenization
- part-of-speech tagging
- advanced linguistic chunking
- hierarchical parse tree generation

## method: analyze_text()
```python
analyze_text(text: str, use_rich: bool = False) -> Dict[str, Any]
```

### return structure
- `overall_stats`: summary metrics
- `sentence_analysis`: per-sentence breakdown
- `phrase_patterns`: recurring linguistic patterns
- `hierarchical_structure`: parse tree representation
- `tree_visualizations`: ascii parse tree view

## chunk object attributes
- `text`: chunk content
- `chunk_type`: linguistic category
- `level`: hierarchical depth
- `position`: chunk location
- `sub_chunks`: nested chunks
- `grammatical_role`: syntactic function

## dependencies
- nltk library
- python 3.7+

## usage example
```python
from srswti_axis import SRSWTIChunkAnalyzer

analyzer = SRSWTIChunkAnalyzer()
results = analyzer.analyze_text("your input text")
```

## performance notes
- uses nltk tokenization
- generates multi-level linguistic representations
- computational complexity: o(n log n)

## additional methods
- `print_pos_tag_legend()`: display pos tag meanings
- `print_grammar_legend()`: show grammar patterns
Sentence: The experienced data scientist RohIT Tiwari quickly analyzed the complex dataset.
S
├── NP
│   ├── The (DT)
│   ├── experienced (JJ)
│   ├── data (NNS)
│   ├── scientist (NN)
│   ├── RohIT (NNP)
│   └── Tiwari (NNP)
├── ADVP
│   └── quickly (RB)
├── VP
│   ├── analyzed (VBD)
│   └── NP
│       ├── the (DT)
│       ├── complex (JJ)
│       └── dataset (NN)
└── . (.)

Sentence: She discovered several interesting patterns in the neural network's behavior.
S
├── CLAUSE
│   ├── NP
│   │   └── She (PRP)
│   └── VP
│       ├── discovered (VBD)
│       └── NP
│           ├── several (JJ)
│           ├── interesting (JJ)
│           └── patterns (NNS)
├── PP
│   ├── in (IN)
│   └── NP
│       ├── the (DT)
│       ├── neural (JJ)
│       └── network (NN)
├── 's (POS)
├── NP
│   └── behavior (NN)
└── . (.)

Sentence: The advanced AI model, despite its limitations, performed exceptionally well on the test cases.
S
├── NP
│   ├── The (DT)
│   ├── advanced (JJ)
│   ├── AI (NNP)
│   └── model (NN)
├── , (,)
├── PP
│   ├── despite (IN)
│   └── NP
│       ├── its (PRP$)
│       └── limitations (NNS)
├── , (,)
├── VP
│   └── performed (VBN)
├── ADVP
│   ├── exceptionally (RB)
│   └── well (RB)
├── PP
│   ├── on (IN)
│   └── NP
│       ├── the (DT)
│       ├── test (NN)
│       └── cases (NNS)
└── . (.)


# srswti ranker 

## overview
document ranking and filtering utility 

## methods

### rank_documents
```python
rank_documents(query: str, candidates: List[str], batch_size: int = 64) -> List[str]
```
ranks documents by similarity to query
- `query`: search input
- `candidates`: documents to rank
- `batch_size`: processing batch size
- returns: sorted documents

### filter_documents
```python
filter_documents(query: str, candidates: List[str], threshold: float = 0.3) -> List[str]
```
filters documents above similarity threshold
- `query`: reference input
- `candidates`: documents to filter
- `threshold`: minimum similarity score
- returns: filtered documents

### get_top_k
```python
get_top_k(query: str, candidates: List[str], k: int = 2) -> List[str]
```
retrieves k most similar documents
- `query`: search input
- `candidates`: document pool
- `k`: number of top documents
- returns: top k similar documents


## usage example
```python
ranker = SrswtiRanker()
results = ranker.rank_documents("search query", candidate_documents)
```

## performance notes
- default batch size: 64
- default similarity threshold: 0.3
- linear time complexity o(n)


# srswti text tools api



## classes

### srswti similarity
compute semantic similarity between text fragments

#### method: compute_similarity
```python
compute_similarity(text1: str, text2: str) -> float
```
- calculates semantic similarity score
- returns value between 0.0 and 1.0
- higher score indicates greater semantic closeness

#### usage example
```python
similarity = SrswtiSimilarity()
score = similarity.compute_similarity("first text", "second text")
```

### srswti splitter
advanced text segmentation and chunk analysis

#### method: split_text
```python
split_text(text: str, target_size: int = 1536) -> List[str]
```
- splits text into semantic chunks
- `target_size`: controls chunk granularity
- returns list of text segments

#### method: get_chunk_info
```python
get_chunk_info(chunks: List[str]) -> Dict[str, Union[List[int], List[str]]]
```
- analyzes text chunk characteristics
- returns dictionary with:
  - `chunk_lengths`: size of each chunk
  - `chunks`: original chunk contents

#### usage example
```python
splitter = SrswtiSplitter()
chunks = splitter.split_text("long text input")
chunk_details = splitter.get_chunk_info(chunks)
```



## performance characteristics
- linear time complexity o(n)
- memory efficient chunk processing
- semantic-aware splitting algorithm

# srswti topic modeling

advanced topic modeling with configurable backends.

## quick start

```python
from srswti_axis import SRSWTIQuasar

model = SRSWTIQuasar(backend='srswti_bi_encoder')
results = model.fit_transform(documents, num_topics=4)
```

## backend configurations

### bi-encoder
```python
model = SRSWTIQuasar(
    backend='srswti_bi_encoder',
    embedding_model='all-MiniLM-L6-v2'
)

# configure model params
model.config = {
    'umap': {
        'n_neighbors': 5,      # tighter clusters
        'n_components': 5,     # dimensions
        'min_dist': 0.0,      # minimum distance
        'metric': 'cosine'    # distance metric
    },
    'hdbscan': {
        'min_cluster_size': 2,  # min cluster
        'min_samples': 1,       # min samples
        'metric': 'euclidean',  # distance
        'cluster_method': 'eom' # cluster method
    }
}

# output example:
{
    'topic_assignments': [-1, 0, 0, 2, ...],  # topic per doc
    'topic_probabilities': [
        [0.8931, 0.0574, 0.0460],  # doc 1
        [1.0000, 0.0000, 0.0000],  # doc 2
        ...
    ]
}
```

### lsa
```python
model = SRSWTIQuasar(backend='srswti_lsa')

# configure params
model.config = {
    'vectorizer': {
        'max_features': 5000,
        'stop_words': 'english'
    },
    'model': {
        'n_components': 'auto',  # dynamic sizing
        'algorithm': 'randomized'
    }
}

# output example:
{
    'document_topic_matrix': [
        [0.4913, 0.4595, -0.1407, 0.0135],  # doc 1
        [0.1801, 0.5029, -0.0667, 0.0311],  # doc 2
        ...
    ],
    'feature_names': ['word1', 'word2', ...],
    'actual_topics': 4
}
```

### matrix factorization
```python
model = SRSWTIQuasar(backend='srswti_nmatrixfact')

# configure params
model.config = {
    'vectorizer': {
        'max_features': 5000
    },
    'model': {
        'init': 'nndsvd',
        'solver': 'cd',
        'beta_loss': 'frobenius'
    }
}

# output example:
{
    'document_topic_matrix': [
        [0.7662, 0.0000, 0.0000, 0.0000],  # doc 1
        [0.5573, 0.0000, 0.0000, 0.0000],  # doc 2
        ...
    ],
    'feature_names': ['word1', 'word2', ...],
    'reconstruction_error': 3.8822
}
```

### latent allocation
```python
model = SRSWTIQuasar(backend='srswti_latent')

# configure params
model.config = {
    'vectorizer': {
        'max_features': 5000
    },
    'model': {
        'learning_method': 'online',
        'learning_decay': 0.7,
        'batch_size': 128
    }
}

# output example:
{
    'document_topic_matrix': [
        [0.0215, 0.0212, 0.9362, 0.0211],  # doc 1
        [0.0229, 0.0229, 0.9312, 0.0230],  # doc 2
        ...
    ],
    'feature_names': ['word1', 'word2', ...],
    'perplexity': 341.2505
}
```

### keyword extraction
```python
model = SRSWTIQuasar(backend='srswti_simple')

# configure params
model.config = {
    'keyphrase_ngram_range': (1, 2),
    'stop_words': 'english',
    'use_maxsum': True,
    'nr_candidates': 20,
    'top_n': 10
}

# output example:
{
    'keywords': [
        [('python programming', 0.763), 
         ('python', 0.692),
         ...],  # doc 1
        [('pattern recognition', 0.578),
         ('learning models', 0.486),
         ...],  # doc 2
        ...
    ]
}
```
# Backend Selection Guide
Choose based on your specific needs:

- **srswti_bi_encoder**: Best for semantic understanding.
- **srswti_lsa**: Fast and effective with large vocabularies.
- **srswti_nmatrixfact**: Provides interpretable topics.
- **srswti_latent**: Utilizes probability-based topic modeling.
- **srswti_simple**: Suitable for basic keyword extraction.

## upcoming features

- custom clustering parameters
- topic number optimization
- model evaluation metrics
- interactive visualization
- streaming processing
- hierarchical topics
- multi-liingual support
- topic coherence scores
- custom preprocessing
- advanced metrics

that's it.