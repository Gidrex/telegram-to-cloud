from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from request_processing import handle_message
from tokens import tg_token, user_data

def main():   
    telegram_token = tg_token()
    mega_email = user_data()[0]
    mega_password = user_data()[1]

    updater = Updater(token=telegram_token, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.document, lambda update, context: handle_message(update, context, mega_email, mega_password)))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
