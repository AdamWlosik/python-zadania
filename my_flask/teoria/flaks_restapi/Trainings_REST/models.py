from __future__ import annotations

from datetime import datetime

from flask_marshmallow import fields

from . import db, ma


class Trainings(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=50), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    note = db.Column(db.String(length=5000), nullable=True)

    def __init__(self, name: str, date: datetime, duration: int, note: str):
        self.name = name
        self.date = date
        self.duration = duration
        self.note = note

    def update(self, modified_training: Trainings) -> None:
        self.name = modified_training.name
        self.date = modified_training.date
        self.duration = modified_training.duration
        self.note = modified_training.note

    @staticmethod
    def create_from_json(json_body: dict) -> Trainings:
        if "date" not in json_body:
            date = datetime.utcnow()
        else:
            date = datetime.strptime(json_body["date"], "%d/%m/%y")

        return Trainings(
            name=json_body["name"],
            date=date,
            duration=json_body["duration"],
            note=json_body["note"],
        )


class TrainingSchema(ma.Schema):
    _id = fields.fields.Integer()
    name = fields.fields.Str()
    date = fields.fields.DateTime(format="%d/%m/%y")
    duration = fields.fields.Integer()
    note = fields.fields.Str()
