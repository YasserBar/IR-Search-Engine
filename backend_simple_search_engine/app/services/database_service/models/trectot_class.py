from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class TrecTotDocument(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doc_id = db.Column(db.Integer)
    page_title = db.Column(db.String(255))
    wikidata_classes = db.Column(db.String(255))
    text = db.Column(db.Text)
    sections = db.Column(db.Text)
    infoboxes = db.Column(db.Text)

    def to_dict(self):
        return {
            'id': self.id,
            'doc_id' : self.doc_id,
            'page_title': self.page_title,
            'wikidata_classes': self.wikidata_classes,
            'text': self.text,
            'sections': self.sections,
            'infoboxes': self.infoboxes,
        }
        
    def get_columns(self, exclude_id):
        columns = self.__table__.columns
        if exclude_id:
            return [column.name for column in columns if column.name != 'id']
        else:
            return [column.name for column in columns]