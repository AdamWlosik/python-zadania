from . import db


class Note(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.String())

    def __init__(self, note):
        self.note = note
