from db import db_session
from models import User, Receipt, Good


def add_user(user_name: str) -> None:
    user = User(name=user_name)
    db_session.add(user)
    db_session.commit()


def get_user(user_id: int) -> str|None:
    if db_session.query(User.query.filter(User.id == user_id).exists()).scalar():
        return User.query.get(user_id)
    else:
        return None


def update_user(user_id: int, user_name: str) -> None:
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


def update_receipt(receipt_id: int, receipt_name: str) -> None:
    receipt = Receipt.query.get(receipt_id)
    receipt.name = receipt_name
    db_session.commit()


def delete_receipt(receipt_id: int) -> None:
    receipt = Receipt.query.get(receipt_id)
    db_session.delete(receipt)
    db_session.commit()


def add_receipt_content(receipt_content: list, receipt_id: int) -> None:
    for good in receipt_content:
        good["receipt_id"] = receipt_id
    db_session.bulk_insert_mappings(Good, receipt_content)
    db_session.commit()


def get_receipt_content(content_id: int) -> str|None:
    if db_session.query(Good.query.filter(Good.id == content_id).exists()).scalar():
        return Good.query.get(content_id)
    else:
        return None    


def delete_receipt_content(content_id: int) -> None:
    content = Good.query.get(content_id)
    db_session.delete(content)
    db_session.commit()
