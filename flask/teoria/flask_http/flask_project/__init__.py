from hashlib import md5  # 0

from flask import Flask


def create_app():
    app = Flask(__name__)
    encryptor = md5()  # 0.1
    app.debug = True
    app.secret_key = encryptor.digest()  # 1

    from .main import dashboard_blueprint, login_blueprint, logout_blueprint

    app.register_blueprint(login_blueprint)
    app.register_blueprint(dashboard_blueprint)
    app.register_blueprint(logout_blueprint)

    return app
