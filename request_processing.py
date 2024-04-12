import os
from mega import Mega
from telegram import Update
from telegram.ext import CallbackContext


def handle_message(update: Update, context: CallbackContext, mega_email, mega_password):
    if update.message.document:
        file = update.message.document.get_file()
        file_path = file.download()

        mega = Mega()
        m = mega.login(mega_email, mega_password)

        try:
            file_name = os.path.basename(file_path)
            m.upload(file_path, dest_filename=file_name)
            update.message.reply_text(f"Файл {file_name} успешно загружен на Mega!")
        except Exception as e:
            update.message.reply_text(f"Ошибка при загрузке файла: {str(e)}")
        finally:
            os.remove(file_path)
    else:
        update.message.reply_text("Пожалуйста, отправьте файл для загрузки на Mega.")
