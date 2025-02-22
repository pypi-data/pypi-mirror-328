from typing import List, Union
import numpy as np
from .core import BM25Indexer, BM25Config
import logging

logger = logging.getLogger(__name__)


class BM25L(BM25Indexer):
    """BM25L: A Better Variant of BM25 for Long Documents

    Reference:
        Yuanhua Lv and ChengXiang Zhai. 2011. Lower-bounding term frequency
        normalization. In Proceedings of CIKM '11. ACM, 7-16.

    The key improvements over standard BM25:
    1. Lower-bounded term frequency normalization
    2. Modified document length normalization
    3. Improved IDF calculation
    """

    def __init__(
        self,
        corpus_or_config: Union[List[List[str]], BM25Config],
        delta: float = 0.5,
        k1: float = 1.2,
        b: float = 0.75,
    ):
        self.delta = float(delta)
        self.epsilon = 1e-10
        super().__init__(corpus_or_config, k1=k1, b=b)
        logger.debug(f"Initialized BM25L: delta={delta}, k1={k1}, b={b}")

    def get_scores(self, query: List[str]) -> np.ndarray:
        """Compute BM25L relevance scores for query terms"""
        scores = np.zeros(self.doc_count, dtype=np.float32)

        # Pre-compute document length factors
        doc_lengths = self.doc_lengths.astype(np.float32)
        avgdl = float(self.avgdl)

        # BM25L parameters
        k1 = float(self.config.k1)
        b = float(self.config.b)

        for term in query:
            if term not in self.term_freqs:
                continue

            # Get term frequencies
            tf = self.term_freqs[term].astype(np.float32)
            df = float(np.count_nonzero(tf))

            if df == 0:
                continue

            N = float(self.doc_count)
            idf = np.log((N - df + 1.0) / (df + 0.5))

            # First normalize by document length
            len_norm = 1.0 - b + b * (doc_lengths / avgdl)
            c_w_d = tf / len_norm

            c_w_d_prime = np.where(
                c_w_d > 0, np.log(1.0 + c_w_d) / np.log(1.0 + self.delta), 0.0
            )

            numerator = c_w_d_prime * (k1 + 1.0)
            denominator = c_w_d_prime + k1
            term_scores = idf * (numerator / np.maximum(denominator, self.epsilon))

            # Debug logging
            logger.debug(f"\nTerm '{term}' scoring details:")
            logger.debug(f"tf={tf}")
            logger.debug(f"df={df}, idf={idf}")
            logger.debug(f"c(w,d)={c_w_d}")
            logger.debug(f"c'(w,d)={c_w_d_prime}")
            logger.debug(f"scores={term_scores}")

            scores += term_scores

        return scores

    def _validate_term_frequencies(self):
        """Validate term frequency data"""
        for term, tf in self.term_freqs.items():
            if not isinstance(tf, np.ndarray):
                raise ValueError(
                    f"Invalid term frequency type for '{term}': {type(tf)}"
                )
            if tf.shape[0] != self.doc_count:
                raise ValueError(
                    f"Invalid term frequency shape for '{term}': {tf.shape}"
                )
            if not np.isfinite(tf).all():
                raise ValueError(f"Invalid term frequency values for '{term}': {tf}")


class BM25Adpt(BM25Indexer):
    """Adaptive BM25 variant that automatically adjusts parameters"""

    def __init__(
        self,
        corpus_or_config: Union[List[List[str]], BM25Config] = None,
        k1: float = 1.2,
        b: float = 0.75,
    ):
        super().__init__(corpus_or_config, k1=k1, b=b)
        self._adapt_parameters()

    def _adapt_parameters(self):
        """Automatically adjust k1 and b based on corpus statistics"""
        if not hasattr(self, "doc_lengths"):
            return

        # Calculate statistics for parameter adjustment
        dl_std = np.std(self.doc_lengths)
        dl_var = np.var(self.doc_lengths)

        # Adjust k1 based on document length variance
        self.config.k1 = 1.2 * (1 + np.log1p(dl_var / self.avgdl))

        # Adjust b based on document length distribution
        self.config.b = 0.75 * (dl_std / self.avgdl)
        # Ensure b stays in reasonable bounds
        self.config.b = max(0.1, min(self.config.b, 0.9))

    def get_scores(self, query: List[str]) -> np.ndarray:
        """Use adapted parameters for scoring"""
        return super().get_scores(query)
