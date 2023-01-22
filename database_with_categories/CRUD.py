from database_with_categories.db import db_session
from database_with_categories.models import User, Receipt,\
    Good, Category, CategoryTriggers
from typing import Any


def add_user(user_name: str) -> int:
    user = User(name=user_name)
    db_session.add(user)
    db_session.commit()
    return user.id


def get_user(user_id: int) -> str | None:
    if db_session.query(
        User.query.filter(User.id == user_id).exists()
                                                     ).scalar():
        return User.query.get(user_id)
    else:
        return None


def add_receipt(receipt_name: str, user_id: int) -> int:
    receipt = Receipt(name=receipt_name, user_id=user_id)
    db_session.add(receipt)
    db_session.commit()
    return receipt.id


def get_receipt(receipt_id: int) -> str | None:
    if db_session.query(
        Receipt.query.filter(Receipt.id == receipt_id).exists()
                                                              ).scalar():
        return Receipt.query.get(receipt_id)
    else:
        return None


def add_receipt_content(receipt_content: list, receipt_id: int) -> None:
    for good in receipt_content:
        good['receipt_id'] = receipt_id
    db_session.bulk_insert_mappings(Good, receipt_content)
    db_session.commit()


def get_receipt_content(receipt_id: int) -> str | None:
    if db_session.query(
        Good.query.filter(Good.id == receipt_id).exists()
                                                        ).scalar():
        return Good.query.get(receipt_id)
    else:
        return None


def add_category(categories: dict[str, Any]) -> list[int]:
    list_to_db = []
    for name_category in categories.keys():
        category = Category(name=name_category)
        list_to_db.append(category)
    db_session.bulk_save_objects(list_to_db)
    db_session.commit()
    results = db_session.scalars(db_session.query(Category.id)).all()
    results = db_session.scalars(
        Category.query.with_entities(Category.id)).all()
    return results[len(results)-len(categories.keys()):]


def add_triggers(categories: dict[str,list], list_of_ids: list[int]) -> None:
    list_to_db = []
    for index, list_triggers in enumerate(categories.values()):
        for trigger in list_triggers:
            temp_dict = {}
            temp_dict['name'] = trigger
            temp_dict['category_id'] = list_of_ids[index]
            list_to_db.append(temp_dict)
    db_session.bulk_insert_mappings(CategoryTriggers, list_to_db)
    db_session.commit()


def get_category(trigger: tuple[str]) -> list[str]:
    query = db_session.query(Category, CategoryTriggers).join(
        Category, CategoryTriggers.category_id == Category.id
    ).filter(CategoryTriggers.name == trigger)
    for category, _ in query:
        break
    return [category.id, category.name]
