from datetime import timedelta
from hashlib import md5

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    # db = SQLAlchemy(app)
    encryptor = md5()

    app.permanent_session_lifetime = timedelta(minutes=30)
    app.secret_key = encryptor.digest()
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    db.init_app(app)

    app.debug = True

    from .main import dashboard_blueprint, login_blueprint, logout_blueprint

    app.register_blueprint(login_blueprint)
    app.register_blueprint(dashboard_blueprint)
    # app.register_blueprint(logout_blueprint)
    app.register_blueprint(logout_blueprint, name="logout")

    return app
