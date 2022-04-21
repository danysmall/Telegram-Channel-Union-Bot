"""Entrypoint of the program."""
from bot import BotFather

API_ID = 7212719
API_HASH = '3778859a51ffe2951f3abe886d03d0f1'
SESSION_NAME = 'bot'


if __name__ == '__main__':
    bot = BotFather(SESSION_NAME, API_ID, API_HASH)
    bot.start()
    print('Hello, world!')
