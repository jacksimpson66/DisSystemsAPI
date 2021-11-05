from app import db


#Module class for db
class Module(db.Model):
    #primary key set
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    #
    lectures = db.relationship('Lecture', backref="module", lazy="dynamic")

    def __repr__(self) -> str:
        return '<Module {}>'.format(self.name)

    #aids with jsonifying data
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }

#Lecture class for db
class Lecture(db.Model):
    #set primary key
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    room = db.Column(db.String(64))
    day = db.Column(db.String(64))
    lecturer = db.Column(db.String(64))
    duration = db.Column(db.Integer)
    #foreign key relationship with module, based on module.id
    module_id = db.Column(db.Integer, db.ForeignKey('module.id'))

    def __repr__(self) -> str:
        return '<Lecture {}>'.format(self.name)

    #aids in jsonifying data
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