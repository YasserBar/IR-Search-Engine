from flask import Flask
from app.config import SQLALCHEMY_DATABASE_URI
from app.config import SQLALCHEMY_TRACK_MODIFICATIONS
from app.services.routes import router

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
app.register_blueprint(router)
