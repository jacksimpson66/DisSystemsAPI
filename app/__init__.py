from abc import abstractproperty
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS

app = Flask(__name__)
#creates REST api object
api = Api(app, catch_all_404s=True)
#sets app configuration
app.config.from_object(Config)
db = SQLAlchemy(app)
#creates migration files for database
migrate = Migrate(app, db)
#Allows CORS
CORS(app, resources={r"*": {"origins": "*"}})

def getApp():
    return app

from app import routes, models