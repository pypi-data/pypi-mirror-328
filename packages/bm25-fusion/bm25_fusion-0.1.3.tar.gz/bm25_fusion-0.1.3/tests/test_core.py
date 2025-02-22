"""
Test cases for BM25 Fusion.
"""

import pytest
from bm25_fusion.core import BM25
from bm25_fusion.tokenization import tokenize

def test_bm25_query():
    """
    Test BM25 query with metadata filter.
    """
    corpus = ["hello world", "machine learning is fun", "hello machine"]
    metadata = [{"category": "news"}, {"category": "science"}, {"category": "news"}]
    bm25 = BM25( metadata=metadata, texts=corpus,\
                 variant="bm25", stopwords={"is", "a", "the", "and"})
    results = bm25.query(["machine"], metadata_filter={"category": "science"}, top_k=2)
    assert len(results) >= 0
    for res in results:
        assert res.get("category") == "science"

def test_bm25_no_stopwords():
    """
    Test BM25 query without stopwords.
    """
    corpus = ["hello world", "machine learning is fun", "hello machine"]
    bm25 = BM25(texts=corpus, variant="bm25")
    results = bm25.query(["machine"], top_k=2)
    assert len(results) >= 0
    assert any("machine" in res["text"] for res in results)

def test_bm25_with_stopwords():
    """
    Test BM25 query with stopwords.
    """
    corpus = ["hello world", "machine learning is fun", "hello machine"]
    bm25 = BM25(texts=corpus, variant="bm25", stopwords={"is", "a", "the", "and"})
    results = bm25.query(["learning"], top_k=2)
    assert len(results) >= 0
    assert any("learning" in res["text"] for res in results)

def test_bm25_empty_query():
    """
    Test BM25 query with empty query.
    """
    corpus = ["hello world", "machine learning is fun", "hello machine"]
    bm25 = BM25(texts=corpus, variant="bm25")
    try:
        bm25.query([], top_k=2)
    except AssertionError as e:
        assert str(e) == "Query tokens cannot be empty."

def test_bm25_metadata_filter():
    """
    Test BM25 query with metadata filter.
    """
    corpus = ["hello world", "machine learning is fun", "hello machine"]
    metadata = [{"category": "news"}, {"category": "science"}, {"category": "news"}]
    bm25 = BM25( metadata=metadata, texts=corpus, variant="bm25")
    results = bm25.query(["hello"], metadata_filter={"category": "news"}, top_k=2)
    assert len(results) >= 0
    for res in results:
        assert res.get("category") == "news"

if __name__ == "__main__":
    pytest.main()
