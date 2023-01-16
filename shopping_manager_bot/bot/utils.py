from settings_box.settings import USER_EMOJI
from emoji import emojize
from random import choice, randint
from telegram import ReplyKeyboardMarkup, KeyboardButton

def main_keyboard():
    return ReplyKeyboardMarkup([
        [
            'Список покупок'
        ]
    ], resize_keyboard=True)


def get_smile(user_data: dict) -> str:
    if 'emoji' not in user_data:
        smile = choice(USER_EMOJI)
        return emojize(smile, language='alias')
    return user_data['emoji']