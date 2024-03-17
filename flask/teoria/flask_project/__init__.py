from flask import Flask


def create_app():
    app = Flask(__name__)
    app.debug = True

    from .main import index_blueprint

    app.register_blueprint(index_blueprint)

    return app
