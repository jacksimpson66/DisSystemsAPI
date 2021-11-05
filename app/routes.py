from flask.helpers import make_response
from flask_migrate import init
from werkzeug.datastructures import V
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

class LoadLectures(Resource):
    def get(self):

        l1 = Lecture(name="Lecture 1", room="WB2.05", day="Monday 10am", lecturer="Ben Stokes", duration=60, module_id=1)
        l2 = Lecture(name="Lecture 2", room="WB2.01", day="Tuesday 10am", lecturer="Ben Stokes", duration=60, module_id=1)
        l3 = Lecture(name="Tutorial 1", room="RS12", day="Thursday 3pm", lecturer="Ben Stokes", duration=60, module_id=1)
        l4 = Lecture(name="Lab 1", room="SM3.5", day="Firday 5pm", lecturer="Mitchell Starc", duration=120, module_id=1)
        l5 = Lecture(name="Lecture 1", room="ND7.6", day="Tuesday 9am", lecturer="Alistair Cook", duration=60, module_id=2)
        l6 = Lecture(name="Lecture 2", room="ND8.0", day="Tuesday 12pm", lecturer="Rashid Khan", duration=60, module_id=2)
        l7 = Lecture(name="Lab 1", room="WB2.03", day="Wednesday 2pm", lecturer="Alistair Cook", duration=120, module_id=2)
        l8 = Lecture(name="Lab 2", room="WB2.04", day="Tuesday 9am", lecturer="Alistair Cook", duration=120, module_id=2)
        l9 = Lecture(name="Lecture 1", room="WB2.02", day="Monday 12pm", lecturer="Babar Azam", duration=60, module_id=3)
        l10 = Lecture(name="Lecture 2", room="WB2.04", day="Tuesday 1pm", lecturer="Babar Azam", duration=60, module_id=3)
        l11 = Lecture(name="Workshop 1", room="ND2.8", day="Thursday 9am", lecturer="Michael Atherton", duration=30, module_id=3)
        l12 = Lecture(name="Lecture 1", room="ND3.7", day="Friday 10am", lecturer="James Anderson", duration=60, module_id=4)
        l13 = Lecture(name="Lab 1", room="RS12", day="Friday 11am", lecturer="James Anderson", duration=120, module_id=4)
        l14 = Lecture(name="Lab 1", room="RS13", day="Monday 4pm", lecturer="Jos Buttler", duration=120, module_id=5)
        l15 = Lecture(name="Lab 2", room="RS21", day="Tuesday 1pm", lecturer="Jonny Bairstow", duration=120, module_id=5)
        l16 = Lecture(name="Tutorial 1", room="SM3.5", day="Tuesday 1pm", lecturer="Jonny Bairstow", duration=60, module_id=5)
        l17 = Lecture(name="Lecture 1", room="SM3.6", day="Tuesday 9am", lecturer="Jason Roy", duration=60, module_id=6)
        l18 = Lecture(name="Lab 1", room="RS13", day="Monday 4pm", lecturer="Tammy Beaumont", duration=60, module_id=6)

        db.session.add(l1)
        db.session.add(l2)
        db.session.add(l3)
        db.session.add(l4)
        db.session.add(l5)
        db.session.add(l6)
        db.session.add(l7)
        db.session.add(l8)
        db.session.add(l9)
        db.session.add(l10)
        db.session.add(l11)
        db.session.add(l12)
        db.session.add(l13)
        db.session.add(l14)
        db.session.add(l15)
        db.session.add(l16)
        db.session.add(l17)
        db.session.add(l18)

        db.session.commit()

api.add_resource(ModulesAPI, '/modules', endpoint='modules')
api.add_resource(LecturesAPI, '/lectures/<int:module_id>', endpoint='lectures')
api.add_resource(LoadLectures, '/loadlectures', endpoint="loadlectures")