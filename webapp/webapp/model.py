from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), index=True, nullable=True, unique=True)
    last_name = db.Column(db.String(50), index=True, nullable=True, unique=True)

    def __repr__(self) -> str:
        return '<User {}>'.format(self.first_name)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), index=True, nullable=True)

    def __repr__(self) -> str:
        return '{}'.format(self.category)
