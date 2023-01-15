from datetime import datetime
from webapp.model import db
from webapp.user.models import User, User_Choice
from webapp.category.models import Category


def save_categories(categories_list: list[str]) -> None:
    """
    Save the category to the database.
    """
    categories = Category(category=categories_list)
    db.session.add(categories)
    db.session.commit()


def create_user(first_name: str, last_name: str, email: str) -> None:
    """
    Save the user to the database.
    """
    user = [{'first_name': first_name, 'last_name': last_name, 'email': email}]
    db.session.bulk_insert_mappings(User, user)
    db.session.commit()


def create_user_choice(select_category, email):
    user = User.query.filter(User.email == email).first()
    date_time_now = datetime.now()
    for category in select_category:
        category_data = Category.query.filter(Category.category == category).first()
        user_choice = [{'user_id': user.id, 'category_id': category_data.id, 'upload': date_time_now.strftime('%Y-%m-%d %H:%M:%S')}]
        db.session.bulk_insert_mappings(User_Choice, user_choice)
        db.session.commit()
