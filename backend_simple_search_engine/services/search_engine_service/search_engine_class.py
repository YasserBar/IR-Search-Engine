
from app.services.search_engine_service.vectorizer_class import Vectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd




class SearchEngine:
    def __init__(self, preprocessor, spell_corrector, document_service, model_service):
        self.preprocessor = preprocessor
        self.spell_corrector = spell_corrector
        self.document_service = document_service
        self.model_service = model_service
        self.last_dataset_name = None
        self.vectorizers = None
        self.tfidf_matrices = None
        self.documents = None
        self.document_count = None
        self.elements = None

    def index_documents(self, dataset_name):
        if self.last_dataset_name == None:
            self.last_dataset_name == dataset_name
        if self.documents == None or self.last_dataset_name != dataset_name:
            self.documents = self.document_service.get_documents(dataset_name)
        if self.elements == None or self.last_dataset_name != dataset_name:
            self.elements = self.document_service.get_columns(dataset_name)
        for element in self.elements:
            if element == 'doc_id':
                continue
            try:
                
                processed_docs = [' '.join(self.preprocessor.preprocess(doc[element])) for doc in self.documents]
                vectorizer = Vectorizer()
                self.vectorizers[element] = vectorizer
                self.tfidf_matrices[element] = vectorizer.fit_transform(processed_docs)
            except Exception as e:
                print(f"An error occurred during vectorization of {element}:", e)
        if self.last_dataset_name != dataset_name:
            self.last_dataset_name == dataset_name

    def save_model(self, name):
        try:
            self.model_service.save_vectorizers(self.vectorizers, name)
            self.model_service.save_tfidf_matrices(self.tfidf_matrices, name)
            len_after = 0
            if self.elements == None or self.last_dataset_name != name:
                self.elements = self.document_service.get_columns(name)
            return {'message': f'{name} vectorizers and tf-idf matrices saved successfully'}, 200
        except ValueError as e:
            return {'message': str(e)}, 400

    def load_model(self, name):
        try:
            self.vectorizers = self.model_service.load_vectorizers(name)
            self.tfidf_matrices = self.model_service.load_tfidf_matrices(name)
            return {'message': f'{name} vectorizers and tf-idf matrices loaded successfully'}, 200
        except ValueError as e:
            return {'message': str(e)}, 400

    def search(self, query, dataset_name, weights=None):
        if self.last_dataset_name == None:
            self.last_dataset_name = dataset_name
        if not self.vectorizers or not self.tfidf_matrices:
            return [], [], query, "Model not loaded"
        
        if weights is None:
            if dataset_name == "trec-tot":
                weights = [0.0, 0.0, 0.0, 1.0, 0.0, 0.0]
            elif dataset_name == "webis-touche":
                weights = [0.0, 0.2, 0.8]
        corrected_query = self.spell_corrector.correct_sentence_spelling(query)
        query_processed = self.preprocessor.preprocess(corrected_query)
        if not query_processed:
            return [], [], corrected_query, "Query could not be processed"
        
        query = ' '.join(query_processed)
        if self.document_count == None or self.last_dataset_name != dataset_name:
            self.document_count = self.document_service.get_document_count(dataset_name)

        scores = np.zeros(self.document_count)
        
        if self.elements == None or self.last_dataset_name != dataset_name:
            self.elements = self.document_service.get_columns(dataset_name)
        cosine_similarities_fields = {
            'page_title': None,
            'wikidata_classes': None,
            'text': None,
            'sections': None,
            'infoboxes': None,
        }
        for element, weight in zip(self.elements, weights):
            if element == "doc_id":
                continue
            try:
                query_vector = self.vectorizers[element].transform(query)
                if query_vector.shape[1] == 0:
                    continue
                cosine_similarities = cosine_similarity(query_vector, self.tfidf_matrices[element]).flatten()
                cosine_similarities_fields[element] = cosine_similarities
                scores += weight * cosine_similarities
            except Exception as e:
                print(f"An error occurred during searching in {element}:", e)

        ranked_indices = np.argsort(scores)[::-1]
        
        if self.last_dataset_name != dataset_name:
            self.last_dataset_name = dataset_name
            
        return ranked_indices, scores, corrected_query, None, cosine_similarities_fields