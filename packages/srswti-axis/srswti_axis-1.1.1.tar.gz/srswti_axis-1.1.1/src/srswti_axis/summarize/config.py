SRSWTI_SUMMARIZATION_MODELS = {
    # Lightweight Models (<200MB)
    "lightweight": {
        "distilbart": {
            "name": "sshleifer/distilbart-cnn-12-6",
            "size": "150MB",
            "best_for": ["production", "mobile", "quick-inference"],
            "params": {
                "min_length": 30,
                "max_length": 150,
                "length_penalty": 1.5,
                "num_beams": 4,
                "early_stopping": True
            }
        }
    },

    # Medium Models (200MB-500MB)
    "medium": {
        "t5_base": {
            "name": "t5-base",
            "size": "220MB",
            "best_for": ["general-purpose", "balanced-performance"],
            "params": {
                "min_length": 40,
                "max_length": 200,
                "length_penalty": 2.0,
                "num_beams": 4,
                "early_stopping": True
            }
        },
        "bart_cnn": {
            "name": "facebook/bart-large-cnn",
            "size": "400MB",
            "best_for": ["news", "articles", "professional-content"],
            "params": {
                "min_length": 50,
                "max_length": 230,
                "length_penalty": 2.0,
                "num_beams": 4,
                "early_stopping": True,
                "no_repeat_ngram_size": 3
            }
        },
        "bart_xsum": {
            "name": "facebook/bart-large-xsum",
            "size": "400MB",
            "best_for": ["extreme-summarization", "headlines"],
            "params": {
                "min_length": 20,
                "max_length": 100,
                "length_penalty": 1.0,
                "num_beams": 6,  # More beams for shorter outputs
                "early_stopping": True
            }
        },
        "pegasus_cnn": {
            "name": "google/pegasus-cnn_dailymail",
            "size": "450MB",
            "best_for": ["news", "balanced-performance"],
            "params": {
                "min_length": 50,
                "max_length": 200,
                "length_penalty": 2.0,
                "num_beams": 4,
                "early_stopping": True
            }
        }
    },

    # Large Models (500MB-1GB)
    "large": {
        "t5_large": {
            "name": "t5-large",
            "size": "800MB",
            "best_for": ["high-quality", "complex-content"],
            "params": {
                "min_length": 50,
                "max_length": 250,
                "length_penalty": 2.0,
                "num_beams": 5,
                "early_stopping": True
            }
        },
        "long_t5": {
            "name": "google/long-t5-tglobal-base",
            "size": "850MB",
            "best_for": ["long-documents", "books", "reports"],
            "params": {
                "min_length": 100,
                "max_length": 1000,
                "length_penalty": 1.5,
                "num_beams": 4,
                "early_stopping": True
            }
        }
    },

    # Extra Large Models (>1GB)
    "xlarge": {
        "mbart": {
            "name": "facebook/mbart-large-cc25",
            "size": "1.1GB",
            "best_for": ["multilingual", "cross-lingual"],
            "params": {
                "min_length": 50,
                "max_length": 200,
                "length_penalty": 1.5,
                "num_beams": 4,
                "early_stopping": True
            }
        },
        "prophetnet": {
            "name": "microsoft/prophetnet-large-uncased",
            "size": "1.6GB",
            "best_for": ["high-quality", "novel-architecture"],
            "params": {
                "min_length": 50,
                "max_length": 250,
                "length_penalty": 2.0,
                "num_beams": 5,
                "early_stopping": True
            }
        },
        "pegasus_large": {
            "name": "google/pegasus-large",
            "size": "2.2GB",
            "best_for": ["state-of-art", "highest-quality"],
            "params": {
                "min_length": 50,
                "max_length": 250,
                "length_penalty": 2.0,
                "num_beams": 8,
                "early_stopping": True,
                "no_repeat_ngram_size": 3
            }
        }
    },

    # Specialized Models
    "specialized": {
        "pegasus_pubmed": {
            "name": "google/pegasus-pubmed",
            "size": "2.2GB",
            "best_for": ["scientific", "medical", "research"],
            "params": {
                "min_length": 150,
                "max_length": 500,
                "length_penalty": 2.0,
                "num_beams": 4,
                "early_stopping": True,
                "no_repeat_ngram_size": 3
            }
        },
        "pegasus_arxiv": {
            "name": "google/pegasus-arxiv",
            "size": "2.2GB",
            "best_for": ["academic", "technical", "research"],
            "params": {
                "min_length": 150,
                "max_length": 500,
                "length_penalty": 2.0,
                "num_beams": 4,
                "early_stopping": True
            }
        }
    }
}

# Long Document Models
SRSWTI_LONG_DOCUMENT_MODELS = {
    "long_document": {
        "long_t5_tglobal": {
            "name": "google/long-t5-tglobal-base",
            "size": "850MB",
            "max_tokens": 16384,
            "best_for": ["books", "long-reports", "documentation"],
            "features": [
                "handles 16k+ tokens",
                "maintains long-range dependencies",
                "efficient memory usage"
            ],
            "params": {
                "min_length": 200,
                "max_length": 1024,
                "length_penalty": 1.5,
                "num_beams": 4,
                "early_stopping": True,
                "no_repeat_ngram_size": 3
            }
        },
        "prophetnet_large": {
            "name": "microsoft/prophetnet-large",
            "size": "1.6GB",
            "max_tokens": 16384,
            "best_for": [
                "long narratives",
                "technical documentation",
                "research papers",
                "books"
            ],
            "features": [
                "novel n-stream self-attention",
                "better long-range understanding",
                "maintains document coherence"
            ],
            "params": {
                "min_length": 150,
                "max_length": 1024,
                "length_penalty": 2.0,
                "num_beams": 5,
                "early_stopping": True,
                "no_repeat_ngram_size": 3
            }
        },
        "big_bird": {
            "name": "google/bigbird-pegasus-large-bigpatent",
            "size": "1.8GB",
            "max_tokens": 4096,
            "best_for": ["patents", "technical documents", "long scientific papers"],
            "features": [
                "sparse attention mechanism",
                "efficient for very long sequences",
                "good at technical content"
            ],
            "params": {
                "min_length": 200,
                "max_length": 1024,
                "length_penalty": 2.0,
                "num_beams": 4,
                "early_stopping": True
            }
        },
        "led_large": {
            "name": "allenai/led-large-16384",
            "size": "1.5GB",
            "max_tokens": 16384,
            "best_for": ["academic papers", "long articles", "multi-section documents"],
            "features": [
                "Longformer architecture",
                "sliding window attention",
                "global attention on key tokens"
            ],
            "params": {
                "min_length": 150,
                "max_length": 1024,
                "length_penalty": 2.0,
                "num_beams": 4,
                "early_stopping": True,
                "global_attention_indices": [0]
            }
        }
    }
}

# Document Type Configurations
LONG_DOCUMENT_CONFIGS = {
    "book_summary": {
        "preferred_model": "long_t5_tglobal",
        "chunk_size": 8192,
        "overlap": 512,
        "min_output_length": 500,
        "max_output_length": 2048,
        "preprocessing": {
            "remove_citations": True,
            "clean_formatting": True
        }
    },
    "technical_doc": {
        "preferred_model": "prophetnet_large",
        "chunk_size": 4096,
        "overlap": 256,
        "min_output_length": 300,
        "max_output_length": 1500,
        "preprocessing": {
            "preserve_code_blocks": True,
            "keep_headers": True
        }
    },
    "research_paper": {
        "preferred_model": "led_large",
        "chunk_size": 4096,
        "overlap": 256,
        "min_output_length": 400,
        "max_output_length": 1500,
        "preprocessing": {
            "remove_references": True,
            "keep_abstract": True,
            "preserve_equations": True
        }
    },
    "patent": {
        "preferred_model": "big_bird",
        "chunk_size": 3072,
        "overlap": 256,
        "min_output_length": 300,
        "max_output_length": 1000,
        "preprocessing": {
            "keep_claims": True,
            "preserve_technical_terms": True
        }
    }
}

# Default System Configuration
DEFAULT_CONFIG = {
    "cache_dir": "./srswti_cache",
    "log_file": "./srswti_summarizer.log",
    "default_batch_size": 4,
    "max_gpu_memory": "12GB",
    "use_fp16": True,
    "enable_progress_bar": True,
    "save_summaries": True,
    "summary_output_dir": "./summaries"
}