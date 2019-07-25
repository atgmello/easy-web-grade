from run import db

class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(50))

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Foreign keys here

class Exam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)
    answers = db.relationship("AnswerSheet", backref="exam", lazy=True)

class AnswerSheet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.String(100))
    exam_id = db.Column(db.Integer, db.ForeignKey("exam.id"))
