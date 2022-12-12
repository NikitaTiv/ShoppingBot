from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

def keyboard_hello() -> ReplyKeyboardMarkup:
    """
    Выводит клавиатуру для пользователя с приветственной кнопкой
    """
    return ReplyKeyboardMarkup([['Привет 👋']], resize_keyboard=True)
    

def keyboard_main_menu() -> ReplyKeyboardMarkup:
    """
    Выводит клаивиату главного меню для пользователя
    """
    return ReplyKeyboardMarkup([['Список покупок 📋', 'Расходы по чеку 💰']], resize_keyboard=True)


def keyboard_operations_with_receipt() -> ReplyKeyboardMarkup:
    """
    Выводит для пользователя меню работы с чеками
    """
    return ReplyKeyboardMarkup([
        ['Добавить чек 🆕', 'Мои чеки 📑', 'Удалить чек 🗑'], 
        ['Возврат в предыдущее меню ↩️']
        ], resize_keyboard=True)


def keyboard_my_receipts() -> InlineKeyboardMarkup:
    """
    Выводит для пользователя в сообщении меню для работы с сохраненными чеками
    """
    return InlineKeyboardMarkup([
        [InlineKeyboardButton('Добавить спонсора', callback_data='1')],
        [InlineKeyboardButton('<<<', callback_data='2'), InlineKeyboardButton('>>>', callback_data='3')],
        [InlineKeyboardButton('Прислать фото чека', callback_data='4')]
        ])