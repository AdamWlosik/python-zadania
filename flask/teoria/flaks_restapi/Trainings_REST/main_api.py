from flask import Blueprint, request

from . import db
from .models import Trainings, TrainingSchema

add_training_blueprint = Blueprint("add_training", __name__)
get_trainings_blueprint = Blueprint("get_trainings", __name__)
get_training_blueprint = Blueprint("get_training", __name__)
update_training_blueprint = Blueprint("update_training", __name__)
delete_training_blueprint = Blueprint("delete_training", __name__)

training_schema = TrainingSchema()
trainings_schema = TrainingSchema(many=True)


def add_to_db(new_training: Trainings) -> None:
    db.session.add(new_training)
    db.session.commit()


def delete_from_db(training_to_delete: Trainings) -> None:
    db.session.delete(training_to_delete)
    db.session.commit()


@add_training_blueprint.route("/trainings", methods=["POST"])
def add_training() -> str:
    body = request.json
    new_training = Trainings.create_from_json(json_body=body)
    add_to_db(new_training)
    return training_schema.jsonify(new_training)


@get_trainings_blueprint.route("/trainings", methods=["GET"])
def get_trainings() -> str:
    all_trainings = Trainings.query.all()
    return trainings_schema.jsonify(all_trainings)


@get_training_blueprint.route("/training/<int:id>", methods=["GET"])
def get_training(id: int) -> str:
    found_training = Trainings.query.get(id)
    return training_schema.jsonify(found_training)


@update_training_blueprint.route("/training/<int:id>", methods=["GET"])
def update_training(id: int) -> str:
    found_training = Trainings.query.get(id)
    body = request.json
    found_training.update(Trainings.create_from_json(json_body=body))
    db.session.commit()
    return training_schema.jsonify(found_training)


@delete_training_blueprint.route("/training/<int:id>", methods=["DELETE"])
def delete_training(id: int) -> str:
    training_to_delete = Trainings.query.get(id)
    delete_from_db(training_to_delete)
    return training_schema.jsonify(training_to_delete)
