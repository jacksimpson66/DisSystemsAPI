from flask.helpers import make_response
from flask_migrate import init
from app import app, db, api
from .models import Module, Lecture
from flask import jsonify, make_response
from flask_restful import Resource, reqparse, abort
import json


class ModulesAPI(Resource):
    def get(self):
        modules = Module.query.all()
        json_to_return = []
        #for each module, use serialize method of class add it to json_to_return, which is then automatically encoded into JSON by Flask-RESTFUL
        for m in modules:
            serialized_module = Module.serialize(m)
            json_to_return.append(serialized_module)
        return json_to_return, 200, {'Access-Control-Allow-Headers':'*'}


class LecturesAPI(Resource):
    def get(self, module_id):
        #check to see if module id exists
        if Lecture.query.filter_by(module_id=module_id).count() < 1:
            abort(404, message=f"Module {module_id} does not exist")

        lectures = Lecture.query.filter_by(module_id=module_id)
        
        json_to_return = []
        #for each lecture returned from query, use serialize method of the class, add to json structure and then return response
        for l in lectures:
            serialized_lecture = Lecture.serialize(l)
            json_to_return.append(serialized_lecture)
        return json_to_return, 200, {'Access-Control-Allow-Headers':'*'}

#add endpoints for REST web service
api.add_resource(ModulesAPI, '/modules', endpoint='modules')
api.add_resource(LecturesAPI, '/lectures/<int:module_id>', endpoint='lectures')

#allow cors
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response