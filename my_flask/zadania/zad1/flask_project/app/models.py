from datetime import datetime
from . import bcrypt


from . import db


class Users(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(100))
    registered_on = db.Column(db.DateTime)

    def __init__(self, username, password):
        self.username = username
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
        self.registered_on = datetime.utcnow()

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
