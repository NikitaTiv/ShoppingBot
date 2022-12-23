from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from db import Base, engine
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String(255), nullable=False)


    def __repr__(self):
        return f'Пользователь id={self.id} - {self.name}'


class Receipt(Base):
    __tablename__ = 'receipt'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)
    date_upload = Column(DateTime(timezone=True), server_default=func.now())
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User")


    def __repr__(self):
        return f'Чек id={self.id} - {self.name} был загружен {self.date_upload} пользователем {self.user_id}'


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)