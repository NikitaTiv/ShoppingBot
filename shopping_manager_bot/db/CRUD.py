from db.db import db_session
from db.models import Good

def add_one_good(user_id: int, good: str) -> None:
    good = Good(user_id=user_id, good=good)
    db_session.add(good)
    db_session.commit()


def get_all_goods(user_id: int) -> list | None:
    return Good.query.filter(Good.user_id == user_id).all()


def delete_all_goods(user_id: int) -> None:
    Good.query.filter(Good.user_id == user_id).delete()
    db_session.commit()


def delete_one_good(content_id: int, user_id: int) -> bool:
    result = Good.query.with_entities(Good.id).filter(Good.user_id == user_id).all()
    for good_id in result:
        if content_id == good_id[0]:
            content = Good.query.get(content_id)
            db_session.delete(content)
            db_session.commit()
            return True
    return None
    