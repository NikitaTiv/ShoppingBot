from sqlalchemy import Column, Integer, String, DateTime
from db import Base, engine


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    name_photo = Column(String)
    date_upload = Column(DateTime)


    def __repr__(self):
        return f'Участник под номером {self.id} - {self.name}'


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)