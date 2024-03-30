from . import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    amount_in_stock = db.Column(db.Integer, nullable=False, default=0)

    def __init__(self, name, amount_in_stock):
        self.name = name
        self.amount_in_stock = amount_in_stock
