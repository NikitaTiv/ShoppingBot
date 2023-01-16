from bot.utils import main_keyboard, get_smile
from db.CRUD import add_one_good, get_all_goods, delete_all_goods, delete_one_good
from telegram import ReplyKeyboardMarkup
from telegram.ext import ConversationHandler

def greet_user(update, context) -> None:
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(
        f'Привет, {update.message.from_user["first_name"]}, Я помогу тебе с покупками! {context.user_data["emoji"]}',
        reply_markup=main_keyboard()
    )


def dialog_start(update, context):
    reply_keyboard = [['Добавить товар', 'Показать список'], ['Удалить один товар', 'Удалить все товары'], ['Выход']]
    update.message.reply_text('Вы вошли в меню работы со списком покупок!\nВыберите пункт меню:', 
                                reply_markup=ReplyKeyboardMarkup(reply_keyboard))
    return 'choose_state'


def dialog_choose_state(update, context):
    if update.message.text == 'Добавить товар':
        update.message.reply_text('Введите название товара и нажмите Ввод')
        return 'add_good'
    elif update.message.text == 'Показать список':
        dialog_get_list_of_goods(update, context)
    elif update.message.text == 'Удалить один товар':
        dialog_get_list_of_goods(update, context)
        update.message.reply_text('Укажите номер id удаляемого сообщения и нажмите Ввод!')
        return 'delete_one_good'
    elif update.message.text == 'Удалить все товары':
        dialog_delete_all_goods(update, context)
    elif update.message.text == 'Выход':
        dialog_skip(update, context)
        happy_end(update, context)
    return ConversationHandler.END


def dialog_add_good(update, context):
    good_name = update.message.text
    if len(good_name) < 3:
        update.message.reply_text('Повторите ввод!')
        return 'add_good'
    add_one_good(update.message.from_user.id, good_name)
    update.message.reply_text('Товар добавлен в базу данных!', reply_markup=main_keyboard())
    return ConversationHandler.END


def happy_end(update, context) -> None:
    update.message.reply_text("Задача выполнена успешно!", reply_markup=main_keyboard())


def dialog_delete_one_good(update, context):
    if delete_one_good(int(update.message.text), update.message.from_user["id"]):
        happy_end(update, context)
    else:
        update.message.reply_text("Ошибка! Повторите попытку!", reply_markup=main_keyboard())   
    return ConversationHandler.END
    

def dialog_delete_all_goods(update, context):
    delete_all_goods(update.message.from_user["id"])
    update.message.reply_text("Список покупок очищен успешно!", reply_markup=main_keyboard())
    return ConversationHandler.END


def dialog_get_list_of_goods(update, context):
    goods_str = "\n".join(map(str, get_all_goods(update.message.from_user["id"])))
    update.message.reply_text(f'Ваш список покупок:\n{goods_str}', reply_markup=main_keyboard())
    return ConversationHandler.END


def dialog_skip(update, context) -> None:
    return ConversationHandler.END


def dialog_fail(update, context):
    update.message.reply_text('Ты прислал что-то не то, напряги извилины и повтори! :)')
