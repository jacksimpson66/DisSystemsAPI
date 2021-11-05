from app import db


#Use flask db migrate to update migration file when changing db
#use flask db upgrade to make changes
#flask db downgrade reverts changes back in time

class Module(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    lectures = db.relationship('Lecture', backref="module", lazy="dynamic")

    def __repr__(self) -> str:
        return '<Module {}>'.format(self.name)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Lecture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    room = db.Column(db.String(64))
    day = db.Column(db.String(64))
    lecturer = db.Column(db.String(64))
    duration = db.Column(db.Integer)
    module_id = db.Column(db.Integer, db.ForeignKey('module.id'))

    def __repr__(self) -> str:
        return '<Lecture {}>'.format(self.name)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'room': self.room,
            'day': self.day,
            'lecturer': self.lecturer,
            'duration': self.duration,
            'module_id': self.module_id
        }