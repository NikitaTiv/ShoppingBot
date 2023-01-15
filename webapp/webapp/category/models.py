from webapp.model import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), index=True, nullable=True)

    def __repr__(self) -> str:
        return '{}'.format(self.category)
