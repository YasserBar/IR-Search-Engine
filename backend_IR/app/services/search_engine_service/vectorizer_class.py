from sklearn.feature_extraction.text import TfidfVectorizer

class Vectorizer:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()

    def fit_transform(self, documents):
        self.tfidf_matrix = self.vectorizer.fit_transform(documents)
        return self.tfidf_matrix

    def transform(self, document):
        return self.vectorizer.transform([document])