from db import db_session
from models import User, Receipt


def add_user(user_name: str) -> None:
    user = User(name=user_name)
    db_session.add(user)
    db_session.commit()


def get_user(user_id: int) -> str|None:
    if db_session.query(User.query.filter(User.id == user_id).exists()).scalar():
        return User.query.get(user_id)
    else:
        return None


def update_user_info(user_id: int, user_name: str) -> None:
    user = User.query.get(user_id)
    user.name = user_name
    db_session.commit()


def delete_user(user_id: int) -> None:
    user = User.query.get(user_id)
    db_session.delete(user)
    db_session.commit()


def add_receipt(receipt_name: str, user_id: int) -> None:
    receipt = Receipt(name=receipt_name, user_id=user_id)
    db_session.add(receipt)
    db_session.commit()


def get_receipt(receipt_id: int) -> str|None:
    if db_session.query(Receipt.query.filter(Receipt.id == receipt_id).exists()).scalar():
        return Receipt.query.get(receipt_id)
    else:
        return None


def update_receipt_info(receipt_id: int, receipt_name: str) -> None:
    receipt = Receipt.query.get(receipt_id)
    receipt.name = receipt_name
    db_session.commit()


def delete_receipt(receipt_id: int) -> None:
    receipt = Receipt.query.get(receipt_id)
    db_session.delete(receipt)
    db_session.commit()
