from utils import main_keyboard, get_smile, play_random_numbers

def greet_user(update, context) -> None:
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(
        f'Привет! Я помогу тебе с покупками! {context.user_data["emoji"]}',
        reply_markup=main_keyboard()
    )


def talk_to_me(update, context) -> None:
    text = update.message.text
    update.message.reply_text(text, reply_markup=main_keyboard())


def guess_number(update, context) -> None:
    if context.args:
        try:
            user_number = int(context.args[0])
            message = play_random_numbers(user_number)
        except (TypeError, ValueError):
            message = 'Введите целое число!'
    else:
        message = 'Введите целое число!'
    update.message.reply_text(message, reply_markup=main_keyboard())


def send_smile(update, context) -> None:
    update.message.reply_text(get_smile(context.user_data), reply_markup=main_keyboard())


def user_coordinates(update, context):
    coords = update.message.location
    update.message.reply_text(coords, reply_markup=main_keyboard())
