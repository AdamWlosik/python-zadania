from flask import Blueprint, redirect, render_template, request, url_for

from . import db
from .models import Note

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
        if "note" in request.form:
            note = request.form["note"]
            add_note = Note(note=note)
            db.session.add(add_note)
            db.session.commit()
    return render_template("add_note.html")


@delete_blueprint.route("/delete_note", methods=["GET", "POST"])
def delete_note_method():
    if request.method == "POST":
        if "note_id" in request.form:
            note_id = request.form["note_id"]
            delete_note = Note.query.get_or_404(note_id)
            db.session.delete(delete_note)
            db.session.commit()
    return render_template("delete_note.html")


@display_blueprint.route("/display_note", methods=["POST"])
def display_note_method():
    notes = Note.query.all()
    return render_template("display_note.html", notes=notes)


@edit_blueprint.route("/edit_note", methods=["POST", "GET"])
def edit_note():
    if request.method == "POST":
        note_id = request.form.get("note_id")
        new_note_content = request.form.get("note")
        if note_id and new_note_content:
            found_note = Note.query.get_or_404(note_id)
            found_note.note = new_note_content
            db.session.commit()
            return redirect(url_for("edit.edit_note"))
    return render_template("edit_note.html")
