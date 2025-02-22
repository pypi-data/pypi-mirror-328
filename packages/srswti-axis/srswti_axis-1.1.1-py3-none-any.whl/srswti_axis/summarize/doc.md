# srswti summarizer

advanced text summarization with configurable models.

## quick start

```python
from srswti_axis import SRSWTISummarizer, SRSWTISummaryConfig

config = SRSWTISummaryConfig(
    model_type="lightweight",
    model_name="srswti_olympus"
)

summarizer = SRSWTISummarizer(config)
result = summarizer.summarize("long text to summarize")
```

## configuration

### basic config
```python
config = SRSWTISummaryConfig(
    model_type="lightweight",    # model size
    model_name="srswti_olympus", # model variant
    device=None,                # auto-select
    use_long_model=False,       # regular mode
    log_file="./logs.log"      # log location
)
```

### model types

# available models
currently we only have olympus for lightweight models
rest you can use from the following configs:

```python
# available types
model_type = [
    "lightweight",  # fast, efficient
    "medium",      # balanced
    "large",       # high quality
    "xlarge",      # best quality
    "specialized"  # domain specific
]

# lightweight models
model_name = [
    "srswti_olympus"  # our custom model
]

# medium models
model_name = [
    "t5-base",                    # general purpose
    "facebook/bart-large-cnn",    # news/articles
    "facebook/bart-large-xsum",   # extreme summarization
    "google/pegasus-cnn_dailymail" # news focused
]

# large models
model_name = [
    "t5-large",                   # high quality
    "google/long-t5-tglobal-base" # long documents
]

# xlarge models
model_name = [
    "facebook/mbart-large-cc25",           # multilingual
    "microsoft/prophetnet-large-uncased",  # high quality
    "google/pegasus-large"                 # state-of-art
]

# specialized models
model_name = [
    "google/pegasus-pubmed",  # medical/scientific
    "google/pegasus-arxiv"    # academic/technical
]



```

### long document handling
```python
config = SRSWTISummaryConfig(
    use_long_model=True,
    long_model_type="book",
    document_type="book_summary"
)
```

## summarization

### basic usage
```python
result = summarizer.summarize(
    text="text to summarize"
)

# returns:
{
    'summaries': ["summarized text"],
    'metadata': {
        'model_type': 'lightweight',
        'model_name': 'SRSWTI-OLYMPUS',
        'num_texts': 1,
        'processing_time': 2.5,
        'device': 'CPU',
        'document_type': None
    }
}
```

### multiple texts
```python
results = summarizer.summarize(
    text=[
        "first text to summarize",
        "second text to summarize"
    ]
)

# returns multiple summaries:
{
    'summaries': [
        "first summary",
        "second summary"
    ],
    'metadata': {...}
}
```

### custom parameters
```python
results = summarizer.summarize(
    text="text to summarize",
    custom_params={
        'max_length': 150,
        'min_length': 50,
        'length_penalty': 2.0
    }
)
```

## long document processing

### chunking config
```python
# document types:
types = {
    'book_summary': {
        'chunk_size': 1000,
        'overlap': 100
    },
    'technical_doc': {
        'chunk_size': 800,
        'overlap': 150
    }
}
```

### chunk processing
```python
# automatic chunking
config = SRSWTISummaryConfig(
    use_long_model=True,
    document_type="book_summary"
)

# processes in chunks:
# 1. splits document
# 2. summarizes chunks
# 3. merges summaries
```

## logging

### log setup
```python
# log file location
config = SRSWTISummaryConfig(
    log_file="./srswti_summarizer.log"
)

# log format:
# timestamp [level] SRSWTI-Summarizer: message
```

### tracked information
```python
# logs include:
- model initialization
- chunk processing
- error states
- completion status
- processing time
```

## memory management

### gpu usage
```python
# automatic gpu detection
config = SRSWTISummaryConfig()  # auto-selects gpu

# force cpu
config = SRSWTISummaryConfig(device="cpu")
```

### cleanup
```python
# automatic cleanup:
- cache clearing
- garbage collection
- resource release
```

## model selection guide

choose based on needs:
- lightweight: fast processing, good quality
- medium: balanced speed/quality
- large: high quality, slower
- xlarge: best quality, resource intensive
- specialized: domain-specific tasks

## output interpretation

summary quality:
- concise: captures main points
- coherent: maintains flow
- complete: preserves key info

metadata usage:
- processing_time: performance metric
- model_type: processing level
- device: resource allocation
- document_type: processing mode

