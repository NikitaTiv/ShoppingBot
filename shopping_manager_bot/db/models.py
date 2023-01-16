from sqlalchemy import Column, Integer, String
from db.db import Base, engine

class Good(Base):
    __tablename__ = 'good'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    good = Column(String, nullable=False)

    def __repr__(self):
        return f'id={self.id}: {self.good}'

def create_model():
    Base.metadata.create_all(bind=engine)
