import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from settings.settings_file import USER_EMOJI
from emoji import emojize
from random import choice, randint
from telegram import ReplyKeyboardMarkup, KeyboardButton

def main_keyboard():
    return ReplyKeyboardMarkup([
        [
            'Список покупок'
        ]
    ])


def get_smile(user_data: dict) -> str:
    if 'emoji' not in user_data:
        smile = choice(USER_EMOJI)
        return emojize(smile, language='alias')
    return user_data['emoji']


def play_random_numbers(user_number: int) -> str:
    bot_number = randint(user_number - 10, user_number + 10)
    if user_number > bot_number:
        message = f'Ваше число {user_number}, мое {bot_number}, Вы выиграли!'
    elif user_number == bot_number:
        message = f'Ваше число {user_number}, мое {bot_number}, Ничья!'
    else:
        message = f'Ваше число {user_number}, мое {bot_number}, Вы проиграли!'
    return message
