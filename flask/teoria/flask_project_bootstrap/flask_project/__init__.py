from flask import Flask


def create_app():
    app = Flask(__name__)
    app.debug = True

    from .main import goodbye_blueprint, welcome_blueprint

    app.register_blueprint(welcome_blueprint)
    app.register_blueprint(goodbye_blueprint)

    return app
