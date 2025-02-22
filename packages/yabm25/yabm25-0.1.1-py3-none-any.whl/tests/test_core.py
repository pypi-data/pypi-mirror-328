import pytest
from yabm25 import BM25Indexer


@pytest.fixture
def sample_corpus():
    return [
        ["hello", "there", "good", "man"],
        ["it", "is", "quite", "windy", "in", "london"],
        ["how", "is", "the", "weather", "today"],
    ]


@pytest.fixture
def bm25(sample_corpus):
    return BM25Indexer(sample_corpus)


def test_initialization(bm25):
    assert bm25.doc_count == 3
    assert bm25.avgdl > 0
    assert len(bm25.lexicon) > 0


def test_get_scores(bm25):
    query = ["windy", "london"]
    scores = bm25.get_scores(query)
    assert len(scores) == 3
    assert scores[1] > scores[0]  # Second document should be most relevant
    assert scores[1] > scores[2]


def test_get_top_n(bm25, sample_corpus):
    query = ["windy", "london"]
    results = bm25.get_top_n(query, sample_corpus, n=1)
    assert len(results) == 1
    assert "windy" in results[0]
    assert "london" in results[0]
