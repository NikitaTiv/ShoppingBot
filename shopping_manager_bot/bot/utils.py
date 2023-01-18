from telegram import ReplyKeyboardMarkup


def main_keyboard():
    return ReplyKeyboardMarkup([
        [
            'Список покупок'
        ]
    ], resize_keyboard=True)
