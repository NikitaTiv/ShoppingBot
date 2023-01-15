from flask_login import UserMixin
from sqlalchemy import ForeignKey

from webapp.model import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), index=True, nullable=True)
    last_name = db.Column(db.String(50), index=True, nullable=True)
    email = db.Column(db.String(100), unique=True)

    def __repr__(self) -> str:
        return '<User {}>'.format(self.first_name)


class User_Choice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey(User.id), nullable=True)
    category_id = db.Column(db.Integer, nullable=True)
    upload = db.Column(db.DateTime, nullable=True)

    def __repr__(self) -> str:
        return '<ID {}>'.format(self.id)