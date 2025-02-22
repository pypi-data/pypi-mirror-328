from yabm25 import BM25Indexer, BM25Config
from pathlib import Path

# Configure disk-based storage
config = BM25Config(
    index_dir=str(Path.home() / "bm25_index"),
    doc_chunk_size=500_000,
    compression="ZSTD",
    memory_map=True
)

# Sample large corpus
large_corpus = [
    ["document", "one", "content"],
    ["document", "two", "content"],
    # ... millions of documents ...
]

try:
    # Build index
    indexer = BM25Indexer(config)
    indexer.build_index(large_corpus)
    
    # Search
    query = ["document", "content"]
    results = indexer.query(query, top_n=10)
    
    print(f"Top matches: {results}")
    
finally:
    indexer.close()
