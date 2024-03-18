from flask import Flask


def create_app():
    app = Flask(__name__)
    app.debug = True

    from .main import login_blueprint, user_blueprint
    app.register_blueprint(login_blueprint)
    app.register_blueprint(user_blueprint)

    return app
