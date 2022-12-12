from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import logging

from handler import (greet_user, main_menu, check_user_photo,
                    spending_on_the_receipt,add_receipt, my_receipts)
import settings

# Создает журнал логов
logging.basicConfig(filename='bot.log', 
    format='[%(asctime)s][%(levelname)s] => %(message)s',
    level=logging.INFO)

# Создаем тело бота
def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    # Добавляем обработчики
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.regex('^(Привет 👋)$'), main_menu))
    dp.add_handler(MessageHandler(Filters.regex('^(Возврат в предыдущее меню ↩️)$'), main_menu))
    dp.add_handler(MessageHandler(Filters.regex('^(Расходы по чеку 💰)$'), spending_on_the_receipt))
    dp.add_handler(MessageHandler(Filters.regex('^(Добавить чек 🆕)$'), add_receipt))
    dp.add_handler(MessageHandler(Filters.regex('^(Мои чеки 📑)$'), my_receipts))
    dp.add_handler(MessageHandler(Filters.photo, check_user_photo))

    mybot.start_polling()
    mybot.idle()

# Запускает бота только в случае, если программа вызвана на прямую
if __name__ == "__main__":
    main()