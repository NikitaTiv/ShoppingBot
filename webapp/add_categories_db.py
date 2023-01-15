from webapp import create_app
from webapp.db_functions import save_categories
from webapp.config import CATEGORY_LIST

for category in CATEGORY_LIST:
    app = create_app()
    with app.app_context():
        save_categories(category)
