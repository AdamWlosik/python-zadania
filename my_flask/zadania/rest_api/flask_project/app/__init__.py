from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        ""  # dane do logowania, ktorych nie pamietam :)
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    app.debug = True

    from .main import (
        create_product_blueprint,
        list_products_blueprint,
        order_product_blueprint,
    )

    app.register_blueprint(create_product_blueprint)
    app.register_blueprint(list_products_blueprint)
    app.register_blueprint(order_product_blueprint)

    return app
