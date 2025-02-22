from yabm25 import BM25Indexer
import re
from typing import List
try:
    import nltk
    from nltk.corpus import stopwords
    from nltk.stem import PorterStemmer
except ImportError:
    print("NLTK is required. Please install it using:")
    print("pip install nltk")
    raise

# Download NLTK data with error handling
def ensure_nltk_data():
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        print("Downloading required NLTK data...")
        nltk.download('stopwords', quiet=True)
    
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        print("Downloading NLTK punkt tokenizer...")
        nltk.download('punkt', quiet=True)

ensure_nltk_data()

class Preprocessor:
    def __init__(self):
        self.stemmer = PorterStemmer()
        self.stop_words = set(stopwords.words('english'))
        
    def preprocess(self, text: str) -> List[str]:
        """Convert text to normalized tokens"""
        # Lowercase and basic cleaning
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        
        # Tokenize
        tokens = text.split()
        
        # Remove stopwords and stem
        tokens = [
            self.stemmer.stem(token)
            for token in tokens
            if token not in self.stop_words
        ]
        
        return tokens

# Example usage
preprocessor = Preprocessor()

corpus = [
    "The quick brown fox jumps over the lazy dog!",
    "A quick brown dog jumps under the happy fox.",
    "The lazy fox sleeps."
]

# Preprocess corpus
processed_corpus = [preprocessor.preprocess(doc) for doc in corpus]
print("\nProcessed corpus:")
for doc in processed_corpus:
    print(doc)

# Create index with processed documents
bm25 = BM25Indexer(processed_corpus)

# Preprocess query the same way
query = "lazy fox sleeping"
processed_query = preprocessor.preprocess(query)
print(f"\nProcessed query: {processed_query}")

# Search
scores = bm25.get_scores(processed_query)
print(f"\nDocument scores: {scores}")

top_docs = bm25.get_top_n(processed_query, corpus, n=1)
print(f"\nTop document: {top_docs}")
