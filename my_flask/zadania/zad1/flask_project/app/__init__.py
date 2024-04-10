from flask import Flask
from hashlib import md5
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)
    encryptor = md5()
    app.secret_key = encryptor.digest()
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    db.init_app(app)
    app.debug = True

    from .main import registration_blueprint, login_blueprint, home_page_blueprint, logout_blueprint

    app.register_blueprint(registration_blueprint)
    app.register_blueprint(login_blueprint)
    app.register_blueprint(home_page_blueprint)
    app.register_blueprint(logout_blueprint)

    return app

