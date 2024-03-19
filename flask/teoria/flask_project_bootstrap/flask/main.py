from flask import Blueprint, render_template

welcome_blueprint = Blueprint("welcome", __name__)
goodbye_blueprint = Blueprint("goodbye", __name__)


# strona główna nie działa dopiero pod adresem http://127.0.0.1:5000/Adam


@welcome_blueprint.route("/welcome/<string:name>")
def welcome(name):
    return render_template("welcome.html", additional_text="Wassup", user_name=name)


@goodbye_blueprint.route("/bye/<string:name>")
def goodbye(name):
    return render_template("goodbye.html", user_name=name)
