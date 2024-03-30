from . import db


class Movies(db.Model):
    """Klasa tworząca bazę danych"""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    opinion = db.Column(db.Text, nullable=True)

    def __init__(self, title: str, opinion: str) -> None:
        self.title = title
        self.opinion = opinion
