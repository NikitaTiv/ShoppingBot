from bot import bot
from db.models import create_model
from settings_box.settings import API_KEY

if __name__ == "__main__":
    create_model()
    bot.main_function(API_KEY=API_KEY)
