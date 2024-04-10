import os

from app import create_app, db


def create_db(app) -> db:
    """Metoda tworząca bazę danych"""
    with app.app_context():
        if not os.path.exists("sqlite:///db.sqlite3"):
            db.create_all()


if __name__ == "__main__":
    app = create_app()
    create_db(app)

    app.run(host="0.0.0.0", port=5010)
