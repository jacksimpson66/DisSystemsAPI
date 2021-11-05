from abc import abstractproperty
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS

app = Flask(__name__)
api = Api(app, catch_all_404s=True)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)

def getApp():
    return app

from app import routes, models