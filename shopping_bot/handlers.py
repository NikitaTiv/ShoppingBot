import os
from random import choice
from telegram import (
    ReplyKeyboardMarkup, ReplyKeyboardRemove, Update,
    InlineKeyboardMarkup, InlineKeyboardButton,
)
from telegram.ext import ConversationHandler, CallbackContext

from utils.clarifai import has_check_on_image_return_bool

import settings


def greet_user(update: Update, context) -> int:
    """Начало разговора."""
    reply_keyboard = [['Привет 👋']]

    user_name = update.message.chat.first_name
    message = f'Привет <b>{user_name}</b>!'
    update.message.reply_text(
        f'{message}', parse_mode='html',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, resize_keyboard=True,
        ),
    )

    return settings.MAIN_MENU


def main_menu(update: Update, context) -> int:
    """Представляет бота пользователю."""
    reply_keyboard = [['Список покупок 📋', 'Расходы по чеку 💰']]

    update.message.reply_text(
        'Я бот Толян 🤖.\nЯ умею составлять списки покупок 🛒'
        '\nи распределять чеки.🙎‍♂️🧾👫',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, resize_keyboard=True,
        ),
    )

    return settings.ACTIONS_WITH_THE_RECEIPT


def operations_with_receipt(update: Update, context) -> int:
    """Представляет пользователю меню для работы с чеками."""
    reply_keyboard = [
        ['Добавить чек 🆕', 'Мои чеки 📑', 'Удалить чек 🗑'],
        ['Возврат в предыдущее меню ↩️'],
    ]
    update.message.reply_text(
        'Выбери категорию 🔎',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, resize_keyboard=True,
        ),
    )

    return settings.MENU_RECEIPT


def add_receipt(update: Update, context) -> int:
    """Представляет пользователю меню для добавления чека."""
    reply_keyboard = [
        ['Возврат в предыдущее меню ↩️'],
    ]

    answer = choice(settings.BOT_ANSWERS)
    update.message.reply_text(
        f'{answer}',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, resize_keyboard=True,
        ))

    return settings.ADD_CHECK


def check_user_photo(update: Update, context: CallbackContext) -> None:
    """
    Проверяет является ли фото присланное пользователем чеком,
    если да, то сохраняет его.
    """
    update.message.reply_text('Обрабатываю фото...')
    os.makedirs('downloads', exist_ok=True)
    photo_file = context.bot.getFile(update.message.photo[-1].file_id)
    file_name = os.path.join('downloads', f'{update.message.photo[-1].file_id}.jpg')
    photo_file.download(file_name)
    if has_check_on_image_return_bool(file_name):
        update.message.reply_text(
            'Обнаружен чек, добавляю фото в библиотеку.',
        )
        os.makedirs('images', exist_ok=True)
        new_filename = os.path.join('images', f'check_{photo_file.file_id}.jpg')
        os.rename(file_name, new_filename)
    else:
        os.remove(file_name)
        update.message.reply_text('Чек на фото не обнаружен.')


def my_receipts(update: Update, context) -> None:
    """
    Открывает пользователю меню с его сохраненными чеками.
    """
    reply_keyboard = [
        [InlineKeyboardButton('Добавить спонсора', callback_data='1')],
        [InlineKeyboardButton('<<<', callback_data='2'), InlineKeyboardButton('>>>', callback_data='3')],
        [InlineKeyboardButton('Прислать фото чека', callback_data='4')],
    ]

    update.message.reply_text('Чек №1', reply_markup=InlineKeyboardMarkup(reply_keyboard, resize_keyboard=True))


def cancel(update: Update, context) -> int:
    """Заканчивает беседу."""
    update.message.reply_text(
        'До Встречи!', reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END
