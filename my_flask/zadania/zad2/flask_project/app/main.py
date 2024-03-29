from flask import Blueprint, render_template, request
from .models import Note
from . import db

home_page_blueprint = Blueprint("home_page", __name__)
add_blueprint = Blueprint("add", __name__)
delete_blueprint = Blueprint("delete", __name__)
display_blueprint = Blueprint("display", __name__)
edit_blueprint = Blueprint("edit", __name__)


@home_page_blueprint.route("/")
def home_page():
    return render_template("home_page.html")


@add_blueprint.route("/add_note", methods=["GET", "POST"])
def add_note_method():
    if request.method == "POST":
        #note = request.form["note"]
        note = "a"
        add_note = Note(note=note)
        db.session.add(add_note)
        db.session.commit()
    return render_template("add_note.html")
