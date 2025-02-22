from yabm25 import BM25Indexer

# Initialize with example corpus
corpus = [
    "Hello there good man!",
    "It is quite windy in London",
    "How is the weather today?"
]

tokenized_corpus = [doc.split(" ") for doc in corpus]

# Create BM25 instance
bm25 = BM25Indexer(tokenized_corpus)

# Test document scoring
query = "windy London"
tokenized_query = query.split(" ")

# Get scores for all documents
doc_scores = bm25.get_scores(tokenized_query)
print("Document scores:", doc_scores)
# Should output: array([0., 0.93729472, 0.])

# Get top documents
top_docs = bm25.get_top_n(tokenized_query, corpus, n=1)
print("\nTop document:", top_docs)
# Should output: ['It is quite windy in London']