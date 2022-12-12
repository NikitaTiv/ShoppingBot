from keyboard import (keyboard_hello, keyboard_main_menu, 
                    keyboard_operations_with_receipt, keyboard_my_receipts)
import os
from random import choice
from telegram import Update
from telegram.ext import CallbackContext, ContextTypes


import settings

def greet_user(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Здоровается с пользователем.
    """
    user_name = update.message.chat.first_name
    message = f"Привет <b>{user_name}</b>!"
    update.message.reply_text(f"{message}", parse_mode='html', reply_markup=keyboard_hello())
    

def main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Представляет бота пользователю
    """
    message = "Я бот Толян 🤖.\nЯ умею составлять списки покупок 🛒\nи распределять чеки.🙎‍♂️🧾👫"
    update.message.reply_text(message, reply_markup=keyboard_main_menu())


def spending_on_the_receipt(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Предлагает пользователю выбрать категорию "Расходы по чеку".
    """
    message = "Выбери категорию 🔎"
    update.message.reply_text(message, reply_markup=keyboard_operations_with_receipt())


def add_receipt(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Предлагает пользователю добавить чек.
    """
    answer = choice(settings.BOT_ANSWERS)
    update.message.reply_text(answer)


def my_receipts(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Открывает пользователю меню с его сохраненными чеками.
    """
    update.message.reply_text('Чек №1', reply_markup=keyboard_my_receipts())


def check_user_photo(update: Update, context: CallbackContext) -> None:
    """
    Сохраняет фото, присланное пользователем в папку downloads
    """
    update.message.reply_text('Обрабатываем фото')
    os.makedirs('downloads', exist_ok=True)
    photo_file = context.bot.getFile(update.message.photo[-1].file_id)
    file_name = os.path.join('downloads', f'{update.message.photo[-1].file_id}.jpg')
    photo_file.download(file_name)
    update.message.reply_text('Фото загружено')