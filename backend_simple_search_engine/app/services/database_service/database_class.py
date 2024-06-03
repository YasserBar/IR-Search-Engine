from app.services.database_service.models.trectot_class import TrecTotDocument
from app.services.database_service.models.webis_touche_class import WebisToucheDocument
from sqlalchemy import inspect

class DocumentService:
    def __init__(self, db):
        self.db = db
        
    def save_document(self, doc_data, dataset_name):
        if dataset_name == "trec-tot":
            doc = TrecTotDocument(
                doc_id=doc_data['doc_id'],
                page_title=doc_data['page_title'],
                wikidata_classes=doc_data['wikidata_classes'],
                text=doc_data['text'],
                sections=doc_data['sections'],
                infoboxes=doc_data['infoboxes']
            )
        elif dataset_name == "webis-touche":
            doc = WebisToucheDocument(
                doc_id=doc_data['doc_id'],
                title=doc_data['title'],
                text=doc_data['text']
            )
        self.db.session.add(doc)
        self.db.session.commit()

    def get_documents(self, dataset_name):
        try:
            if dataset_name == 'trec-tot':
                documents = TrecTotDocument.query.all()
            elif dataset_name == 'webis-touche':
                documents = WebisToucheDocument.query.all()
            else:
                documents = []
            return [doc.to_dict() for doc in documents]
        except Exception as e:
            print("Error occurred while fetching documents :", e)

    def check_data_exists(self, dataset_name):
        table = self.db.metadata.tables.get(dataset_name)
        if table is not None:
            count = self.db.session.query(table).count()
            return count > 0
        
    def check_table_exists(self, dataset_name):
        inspector = inspect(self.db.engine)
        return dataset_name in inspector.get_table_names()
    
    def get_columns(self, dataset_name):
        try:
            if dataset_name == 'trec-tot':
                return TrecTotDocument().get_columns(True)
            elif dataset_name == 'webis-touche':
                return WebisToucheDocument().get_columns(True)
            else:
                return []
        except Exception as e:
            print("Error occurred while fetching document columns:", e)
            
    def get_document_count(self, dataset_name):
        try:
            if dataset_name == 'trec-tot':
                return TrecTotDocument.query.count()
            elif dataset_name == 'webis-touche':
                return WebisToucheDocument.query.count()
            else:
                return 0
        except Exception as e:
            print("Error occurred while fetching document count:", e)
            
    def get_documents_by_indices(self, indices, dataset_name):
        if dataset_name == "trec-tot":
            documents =  TrecTotDocument.query.filter(TrecTotDocument.id.in_(indices)).all()
        elif dataset_name == "webis-touche":
            documents =  WebisToucheDocument.query.filter(WebisToucheDocument.id.in_(indices)).all()
        else:
            documents = []
        return [doc.to_dict() for doc in documents]