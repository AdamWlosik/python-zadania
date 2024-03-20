import os

from app import db


def create_db(app):
    with app.app_context():
        if not os.path.exists("sqlite:///db.sqlite3"):
            db.create_all()


# TODO nie działa problem z baza
