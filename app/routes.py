from flask.helpers import make_response
from flask_migrate import init
from app import app, db, api
from .models import Module, Lecture
from flask import jsonify, make_response
from flask_restful import Resource, reqparse
import json


class ModulesAPI(Resource):
    #deals with get requests for this resource
    def get(self):
        #query all modules
        modules = Module.query.all()
        json_to_return = {
            'modules': []
        }
        #for each module, add it to json_to_return, which is then automatically encoded into JSON by Flask-RESTFUL
        for m in modules:
            serialized_module = Module.serialize(m)
            json_to_return['modules'].append(serialized_module)
        return json_to_return

class LecturesAPI(Resource):
    def get(self, module_id):
        #query lectures with module id given by get request
        lectures = Lecture.query.filter_by(module_id=module_id)
        json_to_return = {
            'lectures': []
        }
        #for each lecture returned from query, add to json structure then return
        for l in lectures:
            serialized_lecture = Lecture.serialize(l)
            json_to_return['lectures'].append(serialized_lecture)
        return json_to_return


api.add_resource(ModulesAPI, '/modules', endpoint='modules')
api.add_resource(LecturesAPI, '/lectures/<int:module_id>', endpoint='lectures')

