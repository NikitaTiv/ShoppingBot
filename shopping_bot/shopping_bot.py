import logging

from telegram.ext import (
    Updater, CommandHandler,
    ConversationHandler, Filters,
    MessageHandler,
)

import settings

from handlers import (
    greet_user, main_menu, operations_with_receipt,
    add_receipt, my_receipts, check_user_photo, cancel,
)

logging.basicConfig(filename='bot.log',
                    format='[%(asctime)s][%(levelname)s] => %(message)s',
                    level=logging.INFO)


def main() -> None:
    """Run the bot."""
    mybot = Updater(settings.API_KEY, use_context=True)

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', greet_user)],
        states={
            settings.MAIN_MENU: [
                MessageHandler(Filters.regex('^(Привет 👋)$'), main_menu),
            ],
            settings.ACTIONS_WITH_THE_RECEIPT: [
                MessageHandler(Filters.regex(
                    '^(Расходы по чеку 💰)$',
                    ), operations_with_receipt),
            ],
            settings.MENU_RECEIPT: [
                MessageHandler(Filters.regex(
                    '^(Добавить чек 🆕)$',
                    ), add_receipt),
                MessageHandler(Filters.regex('^(Мои чеки 📑)$'), my_receipts),
                MessageHandler(Filters.regex(
                    '^(Возврат в предыдущее меню ↩️)$',
                    ), main_menu),
            ],
            settings.ADD_CHECK: [
                MessageHandler(Filters.photo, check_user_photo),
                MessageHandler(Filters.regex(
                    '^(Возврат в предыдущее меню ↩️)$',
                    ), operations_with_receipt),
            ],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dp = mybot.dispatcher
    dp.add_handler(conv_handler)

    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
