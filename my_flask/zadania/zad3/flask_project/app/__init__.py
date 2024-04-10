from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    """Metoda budująca aplikacje"""
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    db.init_app(app)
    app.debug = True

    from .main import (
        add_movie_blueprint,
        home_page_blueprint,
        show_movies_blueprint,
        summary_blueprint,
    )

    app.register_blueprint(add_movie_blueprint)
    app.register_blueprint(show_movies_blueprint)
    app.register_blueprint(home_page_blueprint)
    app.register_blueprint(summary_blueprint)

    return app
