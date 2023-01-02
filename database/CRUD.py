from db import db_session
from models import User, Receipt, Good
from typing import TypedDict


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


receipt_content = [
    {
        "name": "1*: 78032688 СПз Берлинер мал.нач/глазур",
        "price": 144.99,
        "quantity": 1,
        "sum": 144.99
    },
    {
        "name": "2*: 78032687 СПз Берлинер нач.вк.Ман/гл.",
        "price": 144.99,
        "quantity": 1,
        "sum": 144.99
    },
    {
        "name": "3: 3014975 КАРАТ Профитроли ванильные 24",
        "price": 144.99,
        "quantity": 1,
        "sum": 144.99
    },
    {
        "name": "4*: 4010834 OLEA Мыло URBAN жидкое 500мл",
        "price": 144.99,
        "quantity": 1,
        "sum": 144.99
    },
    {
        "name": "5*: 3965705 BUSH.Кофе SENSEI мол.227г",
        "price": 144.99,
        "quantity": 1,
        "sum": 144.99
    },
    {
        "name": "6: 3267348 АРНАУТ Ватруш.дом.твор.изюм20",
        "price": 144.99,
        "quantity": 1,
        "sum": 144.99
    },
    {
        "name": "7: 3257514 КАРАВ.Ватрушка Твор.наслаж.22",
        "price": 144.99,
        "quantity": 1,
        "sum": 144.99
    },
    {
        "name": "8: 4241068 ПАМП.Печ.БЕЛЛ.нач.вк.Йог/М.65",
        "price": 144.99,
        "quantity": 1,
        "sum": 144.99
    },
    {
        "name": "9*: 4088955 МАРК.ПЕР.Яйца кур.стол.С1 20",
        "price": 144.99,
        "quantity": 1,
        "sum": 144.99
    }
]


#if __name__ == "__main__":
#     add_user("Игорь")
#     add_receipt("NewYear2", 2)
#     add_receipt_content(receipt_content, 2)
#   print(get_receipt_content(47))
