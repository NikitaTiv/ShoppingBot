from webapp.model import db, Category, User

def save_categories(categories_list: list[str]) -> None:
    """
    Save the category to the database.
    """
    categories = Category(category=categories_list)
    db.session.add(categories)
    db.session.commit()

def save_user(first_name: str, last_name: str) -> None:
    """
    Save the user to the database.
    """
    user = User(first_name=first_name, last_name=last_name)
    db.session.add(user)
    db.session.commit()