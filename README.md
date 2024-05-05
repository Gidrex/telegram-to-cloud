telegram-to-terrabox

This bot allows you to automatically upload files sent to the chat with the bot to the Mega cloud. To make it work, you need to fill in the files:
mega.txt, where the first line is the email from your MEGA account, and the second is your password
Create a Telegram bot and get its token. This can be done through @BotFather
telegram_token.txt put the token of your Telegram bot into this file

To run the bot, you need Python 3.10

Connect a virtual environment venv by entering commands in the same directory:

```
python3.10 -m venv venv # Creating a virtual environment through the existing directory
source venv/bin/activate # Activating the virtual environment
```

To run the program, write
```
python3.10 main.py
```
