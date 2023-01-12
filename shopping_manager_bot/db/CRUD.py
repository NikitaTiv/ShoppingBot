from db.db import db_session
from db.models import Good

def add_one_good(user_id: int, good: str) -> None:
    good = Good(user_id=user_id, good=good)
    db_session.add(good)
    db_session.commit()


def get_all_goods() -> list | None:
    content = Good.query.all()
    return content


def delete_all_goods() -> None:
    Good.query.delete()
    db_session.commit()


def delete_one_good(content_id: int) -> None:
    content = Good.query.get(content_id)
    db_session.delete(content)
    db_session.commit()
    