from flask import Flask


def create_app():
    app = Flask(__name__)
    app.debug = True

    from .main import app_blueprint, display_forecast_blueprint

    app.register_blueprint(app_blueprint)
    app.register_blueprint(display_forecast_blueprint)

    return app
