from sqlalchemy import Column, Integer, String
from db.db import Base, engine

class Good(Base):
    __tablename__ = 'good'
    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    good = Column(String, nullable=False)

    def __repr__(self):
        return f'id={self.id}: {self.good}'

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
