import pytest
import numpy as np
from yabm25 import BM25L, BM25Adpt
import logging

logging.basicConfig(level=logging.DEBUG)


@pytest.fixture
def test_corpus():
    return [
        ["this", "is", "a", "long", "document"],
        ["short", "doc"],
        ["another", "document", "with", "more", "terms"],
    ]


def test_bm25l():
    """Test BM25L variant with simple case"""
    corpus = [
        ["long", "long", "document", "test"],  # Two occurrences of 'long'
        ["short", "document"],  # No occurrence of 'long'
    ]

    bm25l = BM25L(corpus, delta=0.5, k1=1.2, b=0.75)

    query = ["long"]
    scores = bm25l.get_scores(query)

    # Debug information
    print("\nTest details:")
    print(f"Document lengths: {bm25l.doc_lengths}")
    print(f"Average length: {bm25l.avgdl}")
    print("Term frequencies:")

    # Verify term frequencies are correct
    assert "long" in bm25l.term_freqs, "Term 'long' missing from index"
    tf_long = bm25l.term_freqs["long"]
    print(f"  'long' frequencies: {tf_long}")
    assert tf_long[0] == 2, f"Expected tf=2 for 'long' in doc 1, got {tf_long[0]}"
    assert tf_long[1] == 0, f"Expected tf=0 for 'long' in doc 2, got {tf_long[1]}"

    # Verify scores
    print(f"Raw scores: {scores}")
    assert np.any(scores > 0), f"Expected some non-zero scores, got {scores}"
    assert scores[0] > 0, f"First document score should be > 0, got {scores[0]}"
    assert scores[1] == 0, f"Second document score should be 0, got {scores[1]}"
    assert scores[0] > scores[1], "First document should score higher than second"


def test_bm25adpt():
    corpus = [["doc1", "is", "long"], ["doc2", "is", "short"]]
    bm25adpt = BM25Adpt(corpus)
    scores = bm25adpt.get_scores(["short"])
    assert scores[1] > scores[0]  # Second document should be more relevant for "short"


def test_bm25l_long_documents():
    """Test BM25L behavior with documents of varying lengths"""
    corpus = [
        [
            "document",
            "test",
            "document",
            "test",
            "long",
            "content",
            "more",
            "terms",
            "here",
        ],  # Long doc
        ["short", "doc"],  # Very short doc
        ["document", "test", "here"],  # Medium doc
    ]

    bm25l = BM25L(corpus, delta=0.5, k1=1.2, b=0.75)

    # Debug information
    print("\nDocument statistics:")
    print(f"Lengths: {bm25l.doc_lengths}")
    print(f"Average length: {bm25l.avgdl}")

    # Test with 'document' query
    scores = bm25l.get_scores(["document"])
    print(f"\nScores for 'document': {scores}")

    # Document 0 should get better score due to:
    # 1. Higher term frequency (2 occurrences)
    # 2. BM25L's length normalization
    assert scores[0] > scores[2], (
        f"Long document (score={scores[0]:.4f}) should score higher than "
        f"medium document (score={scores[2]:.4f}) due to BM25L normalization"
    )


def test_bm25adpt_parameter_adjustment():
    corpus = [
        ["short", "text"],
        ["very", "very", "very", "long", "text", "with", "repeated", "terms"],
        ["medium", "sized", "text"],
    ]
    bm25adpt = BM25Adpt(corpus)
    assert hasattr(bm25adpt, "config")
    assert hasattr(bm25adpt.config, "k1")
    assert hasattr(bm25adpt.config, "b")
