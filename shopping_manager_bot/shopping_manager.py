from bot.bot import main_function
from db.models import create_model
from configure.config import API_KEY


if __name__ == "__main__":
    create_model()
    main_function(API_KEY)
