import os

def tg_token():
    if (os.path.getsize("telegram_token.txt") == 0):
        print("Telegram_Bot token issue")
        return 0

    with open("telegram_token.txt", "r") as file:
        token = file.readline().strip()
    return token

def user_data():
    if (os.path.getsize("mega.txt") == 0):
        print("error?")
        return 0        
        
    with open("mega.txt", "r") as file:
        email = file.readline().strip()
        password = file.readline().strip()
    return email, password


