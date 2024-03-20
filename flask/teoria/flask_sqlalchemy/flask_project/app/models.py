from . import db


class Users(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(100), unique=True)

    def __init__(self, name, email):
        self.name, self.email = name, email
