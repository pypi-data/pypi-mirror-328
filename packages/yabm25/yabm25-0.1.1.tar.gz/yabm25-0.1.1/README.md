# YaBM25 - Python BM25 Search Engine

[![PyPI version](https://badge.fury.io/py/yabm25.svg)](https://badge.fury.io/py/yabm25)
[![Python Versions](https://img.shields.io/pypi/pyversions/yabm25.svg)](https://pypi.org/project/yabm25/)
[![Downloads](https://static.pepy.tech/personalized-badge/yabm25?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/yabm25)
[![License](https://img.shields.io/github/license/alimuhammadofficial/yabm25.svg)](https://github.com/alimuhammadofficial/yabm25/blob/main/LICENSE)

Fast, scalable BM25 search engine implementation in Python with both in-memory and disk-based indexing. Perfect for RAG (Retrieval Augmented Generation), information retrieval, and search applications.

## Key Features
- 🚀 **High Performance**: Optimized implementation with vectorized operations
- 💾 **Memory Efficient**: Optional disk-based indexing for large datasets
- 🔄 **rank_bm25 Compatible**: Drop-in replacement for rank_bm25 with extended features
- 📊 **Multiple Variants**: Supports BM25, BM25L, BM25Adpt
- 🛠 **Production Ready**: Thread-safe with proper resource management
- 📦 **Easy Integration**: Works with LangChain, LlamaIndex, and other RAG frameworks

## Benchmarks
| Dataset Size | Memory Usage | Index Time | Query Time |
|-------------|--------------|------------|------------|
|  x  |  y  | z  | qt  |

## Installation
```bash
pip install yabm25
```

## Quick Start

### Simple In-Memory Usage
```python
from yabm25 import BM25Indexer

# Initialize with corpus
corpus = [
    "Hello there good man!",
    "It is quite windy in London",
    "How is the weather today?"
]
tokenized_corpus = [doc.split(" ") for doc in corpus]
bm25 = BM25Indexer(tokenized_corpus)

# Search
query = "windy London"
doc_scores = bm25.get_scores(query.split(" "))
print(doc_scores)  # array([0., 0.93729472, 0.])

# Get top document
top_docs = bm25.get_top_n(query.split(" "), corpus, n=1)
print(top_docs)  # ['It is quite windy in London']
```

### Large-Scale Usage
```python
from yabm25 import BM25Indexer, BM25Config

# Configure disk-based index
config = BM25Config(
    index_dir="my_index",
    doc_chunk_size=500_000,
    compression="ZSTD"
)

# Build index
indexer = BM25Indexer(config)
indexer.build_index(large_corpus)

# Search
results = indexer.query(["term1", "term2"])
```

## Documentation
- [Examples](examples/README.md)
- [API Reference](docs/api.md)
- [Performance Guide](docs/performance.md)

## Use Cases
- 🤖 **RAG Applications**: Enhance LLM responses with relevant context
- 🔍 **Search Systems**: Build powerful document search engines
- 📚 **Information Retrieval**: Academic and research applications
- 📊 **Text Analysis**: Document similarity and ranking

## Comparison with Alternatives
| Feature          | YaBM25 | rank_bm25 | Elasticsearch |
|------------------|--------|-----------|---------------|
| Memory Efficient | ✅     | ❌        | ✅           |
| Disk-based      | ✅     | ❌        | ✅           |
| Easy Setup      | ✅     | ✅        | ❌           |
| Python Native   | ✅     | ✅        | ❌           |
| RAG Optimized   | ✅     | ❌        | ❌           |

## Citation
```bibtex
@software{yabm25,
  title = {YaBM25: Yet Another BM25 Implementation},
  author = {Muhammad, Ali},
  year = {2025},
  url = {https://github.com/alimuhammadofficial/yabm25}
}
```

## Contributing
Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License
MIT License. See [LICENSE](LICENSE) for details.