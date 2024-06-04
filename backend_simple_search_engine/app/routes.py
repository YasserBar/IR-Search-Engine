from app.services.database_service.database_class import DocumentService
from app.services.model_service.model_class import ModelService
from app.services.preprocessor_text_service.preprocessor_text_class import Preprocessor
from app.services.search_engine_service.search_engine_class import SearchEngine
from app.services.spell_corrector_service.spell_corrector_class import SpellCorrector
from flask import Blueprint, request, jsonify
from flask import  request, jsonify
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
preprocessor = Preprocessor()
spell_corrector = SpellCorrector()
document_service = DocumentService(db)
model_service = ModelService(model_directory='./models')
search_engine = SearchEngine(preprocessor, spell_corrector, document_service, model_service)

router = Blueprint('router', __name__)

@router.route('/search/<dataset_name>', methods=['GET'])
def search(dataset_name):
    query = request.args.get('query')
    weights = request.args.get('weights')
    if weights:
        weights = list(map(float, weights.split(',')))
    ranked_indices, scores, corrected_query, error = search_engine.search(query, dataset_name, weights)
    if error:
        return jsonify({'message': error}), 400
    results = []
    for index in ranked_indices:
        results.append(search_engine.documents[index])
    return jsonify({
        'results': results,
        'scores': scores.tolist(),
        'corrected_query': corrected_query
    })


@router.route('/preprocess_text', methods=['GET'])
def preprocess_text():
    text = request.args.get('text')
    preprocessor = Preprocessor()
    cleaned_text = preprocessor.preprocess(text)
    return jsonify({"preprocessed text": cleaned_text}), 200