from __future__ import annotations
import mmap
import struct
import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq
from pathlib import Path
from dataclasses import dataclass
from typing import Dict, List, Tuple, Union
import logging
import concurrent.futures
from collections import defaultdict

logger = logging.getLogger(__name__)


@dataclass
class BM25Config:
    index_dir: str = "index"
    doc_chunk_size: int = 100_000
    postings_chunk_size: int = 1_000_000
    compression: str = "ZSTD"
    k1: float = 1.2
    b: float = 0.75
    memory_map: bool = True


class BM25Indexer:
    def __init__(
        self,
        corpus_or_config: Union[List[List[str]], BM25Config] = None,
        k1: float = 1.2,
        b: float = 0.75,
    ):
        """Initialize with either corpus or config"""
        # Initialize common attributes
        self.lexicon: Dict[str, Tuple[int, int]] = {}
        self.doc_count = 0
        self.avgdl = 0.0

        if isinstance(corpus_or_config, list):
            self.corpus = corpus_or_config
            self.config = BM25Config(k1=k1, b=b)
            self._initialize_in_memory()
        else:
            self.config = corpus_or_config or BM25Config()
            self.corpus = None
            self._initialize_storage()

    def _initialize_in_memory(self):
        """Initialize for in-memory processing"""
        self.doc_lengths = np.array([len(doc) for doc in self.corpus])
        self.doc_count = len(self.corpus)
        self.avgdl = float(np.mean(self.doc_lengths))

        # Build term frequencies
        self.term_freqs = {}

        # Build lexicon for both in-memory and disk-based modes
        term_docs = defaultdict(set)
        for doc_id, doc in enumerate(self.corpus):
            for term in doc:
                if term not in self.term_freqs:
                    self.term_freqs[term] = np.zeros(self.doc_count, dtype=np.float32)
                self.term_freqs[term][doc_id] += 1
                term_docs[term].add(doc_id)

        # Initialize lexicon with document frequencies
        for term, doc_set in term_docs.items():
            self.lexicon[term] = (
                len(doc_set),
                0,
            )  # offset will be updated in disk mode

    def get_scores(self, query: List[str]) -> np.ndarray:
        """Get BM25 scores for all documents"""
        scores = np.zeros(self.doc_count)

        for term in query:
            if term not in self.term_freqs:
                continue

            # Get term frequencies
            term_freq = self.term_freqs[term]
            doc_freq = np.count_nonzero(term_freq)

            # Calculate IDF
            idf = np.log((self.doc_count - doc_freq + 0.5) / (doc_freq + 0.5) + 1.0)

            # Calculate term scores
            k1, b = self.config.k1, self.config.b
            len_norm = 1 - b + b * (self.doc_lengths / self.avgdl)
            numerator = term_freq * (k1 + 1)
            denominator = term_freq + k1 * len_norm
            scores += idf * (numerator / denominator)

        return scores

    def get_top_n(
        self, query: List[str], corpus: List[str] = None, n: int = 5
    ) -> List[str]:
        """Get top N documents for query"""
        scores = self.get_scores(query)
        top_n = np.argsort(scores)[::-1][:n]

        if corpus is None:
            corpus = self.corpus

        return [corpus[i] for i in top_n]

    def _initialize_storage(self):
        """Set up directory structure and file handlers with correct schema"""
        Path(self.config.index_dir).mkdir(exist_ok=True)

        self.schema = pa.schema(
            [
                ("doc_id", pa.int32()),
                ("length", pa.float32()),
                ("terms", pa.list_(pa.string())),
            ]
        )

        self.postings_path = Path(self.config.index_dir) / "postings.bin"
        self.postings_file = open(self.postings_path, "w+b")

        self.doc_writer = pq.ParquetWriter(
            Path(self.config.index_dir) / "documents.parquet",
            schema=self.schema,
            compression=self.config.compression,
        )

        self.lexicon.clear()

    def build_index(self, corpus: List[List[str]]):
        """Build optimized BM25 index from corpus"""
        self._validate_corpus(corpus)
        self._process_documents(corpus)
        self._build_inverted_index(corpus)
        self._write_metadata()
        self._verify_index_integrity()

    def _verify_index_integrity(self):
        """Post-build validation checks"""
        if self.postings_path.stat().st_size == 0:
            raise RuntimeError("Index creation failed - empty postings file")

        if not self.lexicon:
            raise RuntimeError("Index creation failed - empty lexicon")

    def _validate_corpus(self, corpus: List[List[str]]):
        """Ensure corpus meets minimum requirements"""
        if not corpus:
            raise ValueError("Cannot build index with empty corpus")

        for doc in corpus:
            if not isinstance(doc, list):
                raise TypeError("Corpus must be List[List[str]]")
            if not all(isinstance(term, str) for term in doc):
                raise TypeError("Corpus must be List[List[str]]")

    def _process_documents(self, corpus: List[List[str]]):
        """Process and store document metadata"""
        doc_lengths = []
        batch = []

        for doc_id, terms in enumerate(corpus):
            doc_length = float(len(terms))
            doc_lengths.append(doc_length)

            batch.append(
                {"doc_id": doc_id, "length": doc_length, "terms": list(set(terms))}
            )

            if (doc_id + 1) % self.config.doc_chunk_size == 0:
                self._write_document_batch(batch)
                batch = []

        if batch:
            self._write_document_batch(batch)

        self.doc_count = len(corpus)
        self.doc_lengths = np.array(doc_lengths, dtype=np.float32)
        self.avgdl = float(np.mean(doc_lengths))

    def _write_document_batch(self, batch: List[dict]):
        """Write document batch to Parquet with explicit type conversion"""
        doc_ids = pa.array([item["doc_id"] for item in batch], type=pa.int32())
        lengths = pa.array([item["length"] for item in batch], type=pa.float32())
        terms = pa.array([item["terms"] for item in batch], type=pa.list_(pa.string()))

        table = pa.Table.from_arrays([doc_ids, lengths, terms], schema=self.schema)
        self.doc_writer.write_table(table)

    def _build_inverted_index(self, corpus: List[List[str]]):
        """Construct inverted index with enhanced validation"""

        term_postings = defaultdict(list)
        total_terms = 0

        for doc_id, terms in enumerate(corpus):
            if not terms:
                continue

            term_counts = {}
            for term in terms:
                term_counts[term] = term_counts.get(term, 0) + 1

            for term, tf in term_counts.items():
                term_postings[term].append((doc_id, tf))
                total_terms += 1

        if total_terms == 0:
            raise ValueError("Corpus contains no indexable terms")

        self._write_postings(term_postings)

    def _write_postings(self, term_postings: Dict[str, List[Tuple[int, int]]]):
        """Write compressed postings with proper lexicon building"""
        if not term_postings:
            raise RuntimeError("Empty inverted index")

        current_offset = 0
        for term, postings in term_postings.items():
            if not postings:
                continue

            # Sort by doc_id for delta encoding
            postings.sort(key=lambda x: x[0])
            encoded = bytearray()
            prev_doc_id = 0

            # Delta encode postings
            for doc_id, tf in postings:
                delta = doc_id - prev_doc_id
                encoded += struct.pack("II", delta, tf)
                prev_doc_id = doc_id

            # Store term location in lexicon
            if encoded:
                self.lexicon[term] = (len(postings), current_offset)
                self.postings_file.write(encoded)
                current_offset += len(encoded)

        self.postings_file.flush()

    def _write_metadata(self):
        """Persist index metadata"""
        metadata = {
            "doc_count": self.doc_count,
            "avgdl": self.avgdl,
            "lexicon_size": len(self.lexicon),
            "config": vars(self.config),
        }

        with open(Path(self.config.index_dir) / "metadata.npz", "wb") as f:
            np.savez(f, **metadata)

    def query(self, terms: List[str], top_n: int = 10) -> List[Tuple[int, float]]:
        """Execute BM25 query with parallel term processing"""
        scores = np.zeros(self.doc_count, dtype=np.float32)
        idfs = self._calculate_idfs(terms)

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for term, idf in zip(terms, idfs):
                futures.append(executor.submit(self._process_term, term, idf))

            for future in concurrent.futures.as_completed(futures):
                doc_ids, term_scores = future.result()
                np.add.at(scores, doc_ids, term_scores)

        return self._get_top_results(scores, top_n)

    def _calculate_idfs(self, terms: List[str]) -> np.ndarray:
        """Calculate correct BM25 IDF values"""
        idfs = np.zeros(len(terms), dtype=np.float32)

        for i, term in enumerate(terms):
            if term in self.lexicon:
                df = self.lexicon[term][0]  # document frequency
                # Standard BM25 IDF formula: log((N-n+0.5)/(n+0.5))
                idfs[i] = np.log((self.doc_count - df + 0.5) / (df + 0.5))

        return idfs

    def _process_term(self, term: str, idf: float) -> Tuple[np.ndarray, np.ndarray]:
        """Process term with correct BM25 scoring"""
        if term not in self.lexicon or idf == 0:
            return np.array([], dtype=np.int32), np.array([], dtype=np.float32)

        try:
            count, offset = self.lexicon[term]
            with open(self.postings_path, "rb") as f:
                f.seek(offset)
                data = f.read(count * 8)

                doc_ids = np.zeros(count, dtype=np.int32)
                tfs = np.zeros(count, dtype=np.int32)
                current_id = 0

                for i in range(count):
                    delta, tf = struct.unpack_from("II", data, i * 8)
                    current_id += delta
                    doc_ids[i] = current_id
                    tfs[i] = tf

                # Convert to float32 for calculations
                tfs = tfs.astype(np.float32)
                doc_lengths = self.doc_lengths[doc_ids]

                # BM25 scoring
                k1, b = self.config.k1, self.config.b
                len_norm = 1 - b + b * (doc_lengths / self.avgdl)
                numerator = tfs * (k1 + 1)
                denominator = tfs + k1 * len_norm

                scores = numerator / denominator
                return doc_ids, scores * idf

        except Exception as e:
            logger.error(f"Failed to process term '{term}': {str(e)}")
            return np.array([], dtype=np.int32), np.array([], dtype=np.float32)

    def _get_doc_lengths(self, doc_ids: np.ndarray) -> np.ndarray:
        """Retrieve document lengths from Parquet"""
        # Implement optimized length lookup
        return np.array([self.doc_lengths[id] for id in doc_ids], dtype=np.float32)

    def _get_top_results(
        self, scores: np.ndarray, top_n: int
    ) -> List[Tuple[int, float]]:
        """Efficient top-n results extraction"""
        if top_n >= self.doc_count:
            return list(enumerate(scores))

        # Use argpartition for O(n) selection
        partition_idx = np.argpartition(-scores, top_n)[:top_n]
        top_scores = scores[partition_idx]
        sorted_idx = np.argsort(-top_scores)

        return [
            (int(partition_idx[i]), float(top_scores[i]))
            for i in sorted_idx
            if top_scores[i] > 0
        ]

    def close(self):
        """Clean up resources"""
        self.postings_file.close()
        self.doc_writer.close()


class BM25Searcher:
    def __init__(self, index_dir: str = "index"):
        self.config, self.metadata = self._load_index(index_dir)
        self.lexicon = self._load_lexicon()

    def _load_index(self, index_dir: str):
        """Load index metadata and configuration"""
        metadata_path = Path(index_dir) / "metadata.npz"
        with np.load(metadata_path, allow_pickle=True) as data:
            config_dict = data["config"].item()
            metadata = {
                "doc_count": data["doc_count"],
                "avgdl": data["avgdl"],
                "lexicon_size": data["lexicon_size"],
            }
        return BM25Config(**config_dict), metadata

    def _load_lexicon(self):
        """Load lexicon from memory-mapped file"""
        pass
