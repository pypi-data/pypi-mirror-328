# srswti search engine

hybrid neural-probabilistic search system with advanced ranking.

## quick start

```python
from srswti_axis import SRSWTISearchEngine

engine = SRSWTISearchEngine()

documents = [
    "neural networks in machine learning",
    "deep learning architectures",
    "artificial intelligence applications"
]

results = engine.hybrid_search("neural networks", documents)
```

## core components

### initialization
```python
engine = SRSWTISearchEngine(
    embedding_model='srswti-neural-embedder-v1'  # its our own but you can choose your own hf models too
)
```

### hybrid search
```python
results = engine.hybrid_search(
    query="neural networks",
    documents=documents,
    weights={
        'bm25': 0.4,      # probabilistic weight
        'semantic': 0.4,  # neural weight
        'proximity': 0.2  # term proximity weight
    }
)

# returns: [(index, score), ...]
# example: [(0, 0.95), (2, 0.72), (1, 0.45)]
```

### bm25 scoring
```python
scores = engine.calculate_bm25_scores(
    query="neural networks",
    documents=documents
)

# returns: array of scores
# example: [0.82, 0.45, 0.33]
```

### proximity analysis
```python
scores = engine.calculate_proximity_scores(
    query="neural networks",
    documents=documents
)

# returns: array of proximity scores
# example: [0.75, 0.25, 0.15]
```

## advanced usage

### custom weighting
```python
# emphasize semantic search
results = engine.hybrid_search(
    query="neural networks",
    documents=documents,
    weights={
        'bm25': 0.2,
        'semantic': 0.7,
        'proximity': 0.1
    }
)

# emphasize term matching
results = engine.hybrid_search(
    query="neural networks",
    documents=documents,
    weights={
        'bm25': 0.7,
        'semantic': 0.2,
        'proximity': 0.1
    }
)
```

### query expansion
```python
expanded = engine.expand_query(
    "neural networks"
)

# includes:
# - original terms
# - lemmatized forms
# - synonyms
# - related terms
```

### preprocessing
```python
processed = engine.preprocess_text(
    "Deep Learning with Neural Networks"
)

# applies:
# - lowercasing
# - lemmatization
# - stopword removal
# - punctuation removal
```

## scoring components

### bm25
```python
# configuration
engine.bm25_k1 = 1.5  # term saturation
engine.bm25_b = 0.75  # length normalization

# scoring formula:
# score = IDF * (freq * (k1 + 1)) / (freq + k1 * (1 - b + b * doclen/avgdoclen))
```

### semantic scoring
```python
# uses sentence transformers
# - generates embeddings
# - calculates cosine similarity
# - normalizes scores
```

### proximity scoring
```python
# analyzes term positions
# - finds query terms in document
# - calculates minimal distances
# - produces proximity score
```

## output formats

### hybrid search results
```python
[
    (doc_index, score),  # sorted by score
    ...
]

# example:
[
    (0, 0.95),  # best match
    (4, 0.82),  # second best
    (2, 0.67),  # third best
    ...
]
```

### component scores
```python
{
    'bm25_scores': [0.8, 0.6, 0.4],
    'semantic_scores': [0.9, 0.7, 0.5],
    'proximity_scores': [0.7, 0.6, 0.3]
}
```

## score interpretation

bm25 scores:
- higher = better term frequency match
- considers document length
- penalizes common terms

semantic scores:
- higher = better meaning match
- language model based
- context aware

proximity scores:
- higher = terms closer together
- considers term ordering
- local context awareness

## logging and tracking

logs written to:
```
srswti_ir.log
```

format:
```
timestamp [SRSWTI-IR] level: message
```

tracks:
- initialization
- search operations
- preprocessing steps
- scoring calculations
- error states

# srswti hilbert search

learning to rank system with multiple ranking approaches.

## quick start

```python
from srswti_axis import SRSWTIHilbertSearch

# initialize ranker
ranker = SRSWTIHilbertSearch(approach='pointwise')

# train model
ranker.train(
    queries=["deep learning", "neural networks"],
    documents=[
        ["doc1 about dl", "doc2 about dl"],
        ["doc1 about nn", "doc2 about nn"]
    ],
    relevance_scores=[
        [1.0, 0.5],
        [0.8, 0.6]
    ]
)

# rank new documents
results = ranker.rank_documents(
    query="machine learning",
    documents=["doc1", "doc2", "doc3"]
)
```

## ranking approaches

### pointwise ranking
```python
ranker = SRSWTIHilbertSearch(approach='pointwise')

# model architecture:
# input -> linear(64) -> relu -> dropout
#      -> linear(32) -> relu -> dropout
#      -> linear(1) -> sigmoid

# training:
# - direct score prediction
# - mse loss
# - independent document scoring
```

### pairwise ranking
```python
ranker = SRSWTIHilbertSearch(approach='pairwise')

# model architecture:
# input -> linear(64) -> relu -> dropout
#      -> linear(32) -> relu
#      -> linear(1)

# training:
# - document pair comparison
# - binary cross entropy loss
# - relative ordering
```

### listwise ranking
```python
ranker = SRSWTIHilbertSearch(approach='listwise')

# model architecture:
# input -> linear(64) -> relu -> dropout
#      -> linear(32) -> relu
#      -> linear(1) -> softmax

# training:
# - full list scoring
# - cross entropy loss
# - probability distribution
```

## feature extraction

```python
extractor = FeatureExtractor(
    embedding_model='srswti-neural-embedder-v1'
)

features = extractor.extract_features(
    query="query text",
    documents=["doc1", "doc2"]
)

# extracted features:
# - term frequency-idf similarity
# - semantic similarity
# - document length
# - relative length
```

## training

### basic training
```python
ranker.train(
    queries=["q1", "q2"],
    documents=[["d1", "d2"], ["d3", "d4"]],
    relevance_scores=[[1.0, 0.5], [0.8, 0.3]],
    epochs=100
)
```

### pointwise training
```python
# optimize individual scores
loss = mse_loss(predicted_scores, true_scores)
```

### pairwise training
```python
# optimize document pairs
for doc1, doc2 in document_pairs:
    target = 1 if score1 > score2 else 0
    loss = bce_loss(predicted_preference, target)
```

### listwise training
```python
# optimize full ranking
scores = softmax(model_outputs)
loss = cross_entropy(scores, true_distribution)
```

## document ranking

```python
results = ranker.rank_documents(
    query="search query",
    documents=["doc1", "doc2", "doc3"]
)

# returns:
# [(index, score), ...]
# example: [(0, 0.95), (2, 0.72), (1, 0.45)]
```

## model components

### feature extractor
```python
# components:
- embedding model
- term frequency idf vectorizer 
- standard scaler
```

### neural models
```python
# shared architecture:
- input layer (feature dimension)
- hidden layer (64 units)
- dropout (0.2)
- hidden layer (32 units)
- output layer (approach specific)
```

## output formats

### training output
```python
# per epoch:
Epoch 10/100, Loss: 0.2345
Epoch 20/100, Loss: 0.1234
...
```

### ranking output
```python
[
    (doc_index, relevance_score),
    ...
]

# example:
[
    (0, 0.95),  # most relevant
    (4, 0.82),  # second
    (2, 0.67)   # third
]
```

## usage recommendations

choose approach based on needs:
- pointwise: simple, direct scoring
- pairwise: better for relative ordering
- listwise: best for full rankings

memory considerations:
- pointwise: O(n) samples
- pairwise: O(n²) samples
- listwise: O(n) but full list context

training data requirements:
- pointwise: individual scores needed
- pairwise: relative preferences sufficient
- listwise: full ranking information ideal




# srswti search ranker

pagerank-enhanced semantic search engine.

## quick start

```python
from srswti_axis import SRSWTIUltimate

engine = SRSWTIUltimate()

# index documents
documents = [
    "machine learning overview",
    "deep learning concepts",
    "neural networks guide"
]
engine.index_documents(documents)

# search
results = engine.search(
    query="machine learning tutorial",
    n_results=3,
    ranking_method='combined'
)
```

## ranker components

### initialization
```python
ranker = SRSWTISearchRanker(
    embedding_model='srswti-neural-embedder-v1',
    use_pagerank=True
)
```

### document graph
```python
graph = ranker.build_document_graph(
    documents=documents,
    threshold=0.5  # similarity threshold
)

# graph contains:
# - nodes: documents
# - edges: similarity connections
# - weights: cosine similarities
```

### document ranking
```python
results = ranker.rank_documents(
    query="search query",
    documents=documents,
    combine_method='weighted_sum',  # or 'multiplication'
    alpha=0.3  # pagerank weight
)
```

## search engine usage

### indexing
```python
engine = SRSWTIUltimate()
engine.index_documents(documents)

# builds:
# - document graph
# - embeddings
# - pagerank scores
```

### searching
```python
results = engine.search(
    query="search query",
    n_results=5,
    ranking_method='combined'  # or 'multiplication'
)

# returns:
[
    {
        'document': str,     # document text
        'score': float,      # combined score
        'pagerank': float,   # pagerank score
        'cluster': int       # document cluster
    },
    ...
]
```

## ranking methods

### weighted sum
```python
# final_score = α * pagerank + (1-α) * similarity
results = engine.search(
    query="search query",
    ranking_method='combined'
)
```

### multiplication
```python
# final_score = pagerank * similarity
results = engine.search(
    query="search query",
    ranking_method='multiplication'
)
```

## clustering

```python
# get document clusters
clusters = ranker.get_document_clusters()

# returns:
{
    0: [0, 1, 2],  # cluster 0 documents
    1: [3, 4, 5],  # cluster 1 documents
    ...
}
```

## advanced features

### graph customization
```python
# custom similarity threshold
graph = ranker.build_document_graph(
    documents=docs,
    threshold=0.7  # stricter connections
)
```

### score combination
```python
# adjust pagerank influence
results = ranker.rank_documents(
    query=query,
    documents=docs,
    alpha=0.5  # equal weighting
)
```

### result filtering
```python
# get specific cluster
results = engine.search(
    query=query,
    n_results=5
)
cluster_docs = [r for r in results 
               if r['cluster'] == 0]
```

## output formats

### search results
```python
[
    {
        'document': 'text content...',
        'score': 0.85,           # total score
        'pagerank': 0.23,        # graph score
        'cluster': 1             # group id
    },
    ...
]
```

### ranking scores
```python
[
    (doc_index, score),
    ...
]

# example:
[
    (0, 0.95),  # best match
    (4, 0.82),  # second best
    (2, 0.67)   # third best
]
```

## score interpretation

combined score:
- range: 0 to 1
- higher = more relevant
- considers both connections and content

pagerank score:
- range: 0 to 1
- higher = more central
- based on document connections

cluster id:
- -1: isolated document
- 0+: connected component

