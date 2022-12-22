from db import db_session
from models import User
import datetime


def add_user_info(input_name: str, input_name_photo: str) -> None:
    user = User(name=input_name, name_photo=input_name_photo, date_upload = datetime.datetime.now())
    db_session.add(user)
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