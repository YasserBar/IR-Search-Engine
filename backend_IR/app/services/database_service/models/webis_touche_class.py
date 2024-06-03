from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class WebisToucheDocument(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doc_id = db.Column(db.String(255))
    title = db.Column(db.String(255))
    text = db.Column(db.Text)

    def to_dict(self):
        return {
            'id': self.id,
            'doc_id' : self.doc_id,
            'title': self.title,
            'text': self.text,
        }
        
    def get_columns(self, exclude_id):
        columns = self.__table__.columns
        if exclude_id:
            return [column.name for column in columns if column.name != 'id']
        else:
            return [column.name for column in columns]