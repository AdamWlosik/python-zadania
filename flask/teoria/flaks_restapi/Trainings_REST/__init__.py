from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from flask import Flask

db = SQLAlchemy()
ma = Marshmallow()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///trainings.sqlite3"

    db.init_app(app)
    ma.init_app(app)

    from .main_api import (
        add_training_blueprint,
        delete_training_blueprint,
        get_training_blueprint,
        get_trainings_blueprint,
        update_training_blueprint,
    )

    app.register_blueprint(add_training_blueprint)
    app.register_blueprint(get_trainings_blueprint)
    app.register_blueprint(get_training_blueprint)
    app.register_blueprint(update_training_blueprint)
    app.register_blueprint(delete_training_blueprint)

    return app
