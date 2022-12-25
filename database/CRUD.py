from db import db_session
from models import User, Receipt


def add_user(user_name: str) -> None:
    user = User(name=user_name)
    db_session.add(user)
    db_session.commit()


def get_user_info(input_id: int) -> str|None:
    if db_session.query(User.query.filter(User.id == input_id).exists()).scalar():
        user = User.query.get(input_id)
        return f'Имя пользоватя id №{input_id} - {user.name}'
    else:
        return None


def update_user_info(input_id: int, input_name: str) -> None:
    user = User.query.get(input_id)
    user.name = input_name
    db_session.commit()


def delete_user(input_id: int) -> None:
    user = User.query.get(input_id)
    db_session.delete(user)
    db_session.commit()


def add_receipt(receipt_name: str, input_user_id: int) -> None:
    receipt = Receipt(name=receipt_name, user_id=input_user_id)
    db_session.add(receipt)
    db_session.commit()


def get_receipt_info(input_id: int) -> str|None:
    if db_session.query(Receipt.query.filter(Receipt.id == input_id).exists()).scalar():
        receipt = Receipt.query.get(input_id)
        user = User.query.get(receipt.user_id)
        return(f'Чек id №{input_id} с названием "{receipt.name}" загружен пользователем id №{receipt.user_id} по имени {user.name} {receipt.date_upload}')
    else:
        return None


def update_receipt_info(input_id: int, input_name: str) -> None:
    receipt = Receipt.query.get(input_id)
    receipt.name = input_name
    db_session.commit()


def delete_receipt(input_id: int) -> None:
    receipt = Receipt.query.get(input_id)
    db_session.delete(receipt)
    db_session.commit()
