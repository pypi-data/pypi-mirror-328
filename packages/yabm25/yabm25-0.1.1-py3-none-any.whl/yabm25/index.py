from typing import Dict, Any, List
from .core import BM25Config, BM25Indexer


class IndexManager:
    def __init__(self, config: BM25Config = BM25Config()):
        self.config = config
        self.indexer = BM25Indexer(config)

    def create_index(self, corpus: List[List[str]]):
        """Create new search index"""
        self.indexer.build_index(corpus)
        self.indexer.close()

    def optimize_index(self):
        """Optimize index for query performance"""
        pass

    def backup_index(self, destination: str):
        """Create backup of index files"""
        pass

    def get_index_stats(self) -> Dict[str, Any]:
        """Return index statistics"""
        return {
            "document_count": self.indexer.doc_count,
            "average_length": self.indexer.avgdl,
            "lexicon_size": len(self.indexer.lexicon),
        }
