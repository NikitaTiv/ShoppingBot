from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float
from db import Base, engine
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)

    def __repr__(self):
        return f'Пользователь id={self.id} - {self.name}'


class Receipt(Base):
    __tablename__ = 'receipt'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)
    date_upload = Column(DateTime(timezone=True), server_default=func.now())
    user_id = Column(Integer, ForeignKey("user.id"), index=True)
    user = relationship("User")

    def __repr__(self):
        return f'Чек id={self.id} - "{self.name}" был загружен {self.date_upload} пользователем id={self.user_id}'


class Good(Base):
    __tablename__ = 'good'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float)
    quantity = Column(Integer)
    sum = Column(Float)
    receipt_id = Column(Integer, ForeignKey("receipt.id"), index=True)
    receipt = relationship("Receipt")

    def __repr__(self):
        return f'Чек id={self.receipt_id}\nid товара={self.id}\nНазвание={self.name}\nЦена={self.price}\nКоличество={self.quantity}\nСтоимость={self.sum}'


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
