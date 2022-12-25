from db import db_session
from models import User, Receipt


def add_user(user_name: str) -> None:
    user = User(name=user_name)
    db_session.add(user)
    db_session.commit()


def add_receipt(receipt_name: str, input_user_id: int) -> None:
    receipt = Receipt(name=receipt_name, user_id=input_user_id)
    db_session.add(receipt)
    db_session.commit()


def get_user_info(input_id: int) -> str:
    user = User.query.get(input_id)
    print(f"""
    Имя {user.name}
    Этот пользователь загрузил фото ---{user.name_photo}---
    и произошло это {user.date_upload}
    """)


def update_user_info(input_id: int, input_name: str, input_name_photo: str) -> None:
    user = User.query.get(input_id)
    user.name = input_name
    user.name_photo = input_name_photo
    db_session.commit()


def delete_user(input_id: int) -> None:
    user = User.query.get(input_id)
    db_session.delete(user)
    db_session.commit()