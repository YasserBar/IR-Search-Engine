import joblib
import os

class ModelService:
    def __init__(self, model_directory):
        self.model_directory = model_directory
        if not os.path.exists(model_directory):
            os.makedirs(model_directory)

    def save_vectorizers(self, vectorizers, name):
        try:
            vectorizer_path = os.path.join(self.model_directory, name + '_vectorizers.pkl')
            with open(vectorizer_path, 'wb') as file:
                joblib.dump(vectorizers, file)
            print(f'{name}_vectorizers.pkl saved successfully')
        except ValueError as e:
            print(f'{name}_vectorizers.pkl could not be saved:', e)

    def save_tfidf_matrices(self, tfidf_matrices, name):
        try:
            tfidf_path = os.path.join(self.model_directory, name + '_tfidf_matrices.pkl')
            with open(tfidf_path, 'wb') as file:
                joblib.dump(tfidf_matrices, file)
            print(f'{name}_tfidf_matrices.pkl saved successfully')
        except ValueError as e:
            print(f'{name}_tfidf_matrices.pkl could not be saved:', e)

    def load_vectorizers(self, name):
        try:
            vectorizer_path = os.path.join(self.model_directory, name + '_vectorizers.pkl')
            with open(vectorizer_path, 'rb') as file:
                return joblib.load(file)
        except ValueError as e:
            print(f'{name}_vectorizers.pkl could not be loaded:', e)
            return None

    def load_tfidf_matrices(self, name):
        try:
            tfidf_path = os.path.join(self.model_directory, name + '_tfidf_matrices.pkl')
            with open(tfidf_path, 'rb') as file:
                return joblib.load(file)
        except ValueError as e:
            print(f'{name}_tfidf_matrices.pkl could not be loaded:', e)
            return None