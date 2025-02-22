# srswti zero-shot classifier

## quick start

```python
from srswti_axis import SRSWTIZeroShot

classifier = SRSWTIZeroShot()
result = classifier.classify_text(
    "the new ai model is impressive but has high compute needs",
    ["tech", "science", "economics"]
)
```

## core concepts

### classification approach

we use a clever transformer-based approach that turns classification into an entailment problem. it's like asking "is this text about X?" instead of forcing it into predefined boxes.

### probability transformations

#### multi-label scenario
when you want multiple labels (because why not?), we use:

$p(y_i|x) = \frac{1}{1 + e^{-z_i}}$

this lets each label decide for itself. no fighting between labels, just pure independence.

#### single-label classification
when you need that one perfect label:

$p(y_i|x) = \frac{e^{z_i}}{\sum e^{z_j}}$

forces labels to compete. may the best label win.

## api

### classifier initialization
```python
classifier = SRSWTIZeroShot(
    device=None,        # auto-picks "rocm"/cuda/mps/cpu
    batch_size=8,       # process multiple texts at once
    model_name="SRSWTI-ZeroShot-v1"
)
```

### classification methods

#### single text classification
```python
result = classifier.classify_text(
    text="impressive performance but high costs",
    candidate_labels=["positive", "negative", "neutral"],
    multi_label=False  # set True if you want multiple labels
)
```

text (str): Input text to classify
candidate_labels (List[str]): Possible classification labels
multi_label (bool): Enable multi-label classification

#### batch processing
```python
tasks = [{
    "name": "product reviews",
    "texts": ["amazing product!", "terrible experience"],
    "labels": ["positive", "negative", "neutral"],
    "multi_label": False
}]

classifier.process_tasks(tasks)

process_tasks
pythonCopydef process_tasks(
    self,
    tasks: List[Dict[str, Union[str, List[str], bool]]]
)
Parameters:

tasks: List of task dictionaries with structure:
pythonCopy{
    "name": str,          # Task identifier
    "texts": List[str],   # Texts to classify
    "labels": List[str],  # Candidate labels
    "multi_label": bool   # Multi-label flag
}
```

## features

-  zero-shot: no training needed
-  batch processing: because speed matters
-  multi-label support: why choose one?

## under the hood
go to sauce page for the math behind it

## practical stuff

### memory usage
- batch_size=8: ~2gb vram
- cpu mode: scales with batch_size

### speed tips
```python
classifier = SRSWTIZeroShot(batch_size=16, device="cuda")

classifier = SRSWTIZeroShot(batch_size=4, device="cpu")
```


## limits

- texts: max 512 tokens, chunk it and process them--- still faster than llms digesting 50000 tokens as chunks at once
- no other limits.

## coming soon

- better custom models
- api interface, for free. with rate limits and batch_size=1
- more logging options
- custom tokenizers, multilingual ones too.

## notes
that's it. let the classifier do its thing.