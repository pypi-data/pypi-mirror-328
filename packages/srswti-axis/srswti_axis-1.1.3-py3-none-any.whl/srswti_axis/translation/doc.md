# srswti multilingual translator

multilingual translation with comprehensive language support.

## quick start

```python
from srswti_axis import SRSWTIMultilingualTranslator

translator = SRSWTIMultilingualTranslator()

result = translator.translate_text(
    text="Hello, world!",
    src_lang="English",
    tgt_lang="French"
)
```

## supported languages

```python
languages = {
    'English': 'en',      'Spanish': 'es', 
    'French': 'fr',       'German': 'de',
    'Italian': 'it',      'Portuguese': 'pt',
    'Russian': 'ru',      'Chinese': 'zh',
    'Japanese': 'ja',     'Korean': 'ko',
    'Arabic': 'ar',       'Hindi': 'hi',
    'Dutch': 'nl',        'Polish': 'pl',
    'Turkish': 'tr'
}
```

## initialization

### basic setup
```python
# auto device selection
translator = SRSWTIMultilingualTranslator()

# specific device
translator = SRSWTIMultilingualTranslator(
    device="cuda"  # or "cpu", "mps",  "rocm"
)
```

### custom config
```python
translator = SRSWTIMultilingualTranslator(
    device="cuda",
    config={
        # custom settings
    }
)
```

## translation

### basic translation
```python
result = translator.translate_text(
    text="Hello, world!",
    src_lang="English",
    tgt_lang="French"
)

# returns:
{
    'translation': 'Bonjour, monde!',
    'metadata': {
        'source_language': 'English',
        'target_language': 'French',
        'processing_time': 0.5432,
        'model': 'SRSWTI-Multilingual-en-fr',
        'device': 'CUDA',
        'timestamp': '2025-02-13 12:34:56'
    }
}
```

### error handling
```python
# invalid language
result = translator.translate_text(
    text="Hello",
    src_lang="Invalid",
    tgt_lang="French"
)

# returns:
{
    'translation': None,
    'error': 'Invalid language selection!'
}
```

## result display

### formatted output
```python
from srswti_axis import print_translation_results

print_translation_results(result)

# displays:
SRSWTI Multilingual Translation Results
==================================================
• Source Language:   English
• Target Language:   French
• Processing Time:   0.5432 seconds
• Device:           CUDA
• Timestamp:        2025-02-13 12:34:56
• Model:            SRSWTI-Multilingual-en-fr

Translation:
--------------------------------------------------
Bonjour, monde!
```

## example translations

### multiple languages
```python
examples = [
    {
        "text": "AI advances rapidly",
        "from": "English",
        "to": "Japanese"
    },
    {
        "text": "La tecnología evoluciona",
        "from": "Spanish",
        "to": "German"
    }
]

for example in examples:
    result = translator.translate_text(
        text=example["text"],
        src_lang=example["from"],
        tgt_lang=example["to"]
    )
```

### complex text
```python
long_text = """
Artificial intelligence has transformed 
modern technology, enabling unprecedented 
advances in various fields.
"""

result = translator.translate_text(
    text=long_text,
    src_lang="English",
    tgt_lang="Chinese"
)
```

## logging

### log format
```
timestamp [level] SRSWTI-Multilingual-Translator: message
```

### tracked information
```python
# logs include:
- initialization
- model loading
- translation process
- errors/warnings
- completion status
```

## memory management

### model caching
```python
# models cached by language pair:
translators = {
    'en-fr': model,  # english to french
    'es-en': model,  # spanish to english
    ...
}
```

### resource cleanup
```python
# automatic cleanup:
- model unloading
- memory optimization
```

## usage tips

language pairs:
- use full names: "English" not "en"
- case sensitive: "French" not "french"
- verify support before use

performance:
- models cached after first use
- batch similar language pairs

output handling:
- always check for errors
- use metadata for tracking
- format output as needed

