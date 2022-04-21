"""Entrypoint of the program."""
from bot import BotFather


if __name__ == '__main__':
    bot = BotFather('settings.cfg')
    bot.start()
    print('Hello, world!')
