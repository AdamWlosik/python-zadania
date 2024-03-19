from flask import Blueprint, render_template

index_blueprint = Blueprint("index", __name__)


@index_blueprint.route("/<string:name>")
def index(name):
    return render_template("index.html", welcome_text="Wassup", user_name=name)
