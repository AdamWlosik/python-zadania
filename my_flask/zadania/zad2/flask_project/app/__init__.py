from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    db.init_app(app)
    app.debug = True

    from .main import home_page_blueprint, add_blueprint, delete_blueprint, display_blueprint, edit_blueprint

    app.register_blueprint(home_page_blueprint)
    app.register_blueprint(add_blueprint)
    app.register_blueprint(delete_blueprint)
    app.register_blueprint(display_blueprint)
    app.register_blueprint(edit_blueprint)

    return app
