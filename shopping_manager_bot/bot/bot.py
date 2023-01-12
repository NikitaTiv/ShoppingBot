import logging, os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from settings.settings_file import API_KEY
from telegram.ext import CommandHandler, Updater, MessageHandler, Filters, ConversationHandler
from dialog import dialog_start, dialog_add_good, dialog_fail, dialog_choose_state, dialog_delete_one_good
from handlers import greet_user

logging.basicConfig(filename='bot.log', level=logging.INFO)

def main_function() -> None:
    shopping_manager_bot = Updater(API_KEY, use_context=True)
    dp = shopping_manager_bot.dispatcher
    dialog_structure = ConversationHandler(
        entry_points=[ #какие могут быть "входные точки"
            MessageHandler(Filters.regex('^(Список покупок)$'), dialog_start)
        ],
        states={ #список возможных состояний конечного автомата
            'add_good': [MessageHandler(Filters.text, dialog_add_good)],
            'choose_state': [MessageHandler(Filters.text, dialog_choose_state)],
            'delete_one_good': [MessageHandler(Filters.text, dialog_delete_one_good)],
        },
        fallbacks=[
            MessageHandler(Filters.text | Filters.photo | Filters.video | Filters.document | Filters.location, dialog_fail)
        ] #ловушки для неверных ответов
    )
    dp.add_handler(dialog_structure)
    dp.add_handler(CommandHandler('start', greet_user))
    shopping_manager_bot.start_polling()
    shopping_manager_bot.idle()

if __name__ == "__main__":
    main_function()
