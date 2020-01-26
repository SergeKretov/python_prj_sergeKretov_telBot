#Must be installed python-telegram-bot lib.
from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters
import os

TOKEN = os.environ.get('serge_kretov_tel_bot') #bot token from @botFather in config vars on heroku.com


def message_handler(bot:Bot, update:Update):
    user = update.effective_user
    if user:
        name = user.first_name
    else:
        name = 'аноним'

    text = update.effective_message.text
    if text == '/start':
        txt1 = 'Я виртуальный помощник Сергея из Юридического агентства ПРИОРИТЕТ.'
        reply_text = f'Привет, {name}!\n\n{txt1}'
    else:
        reply_text = f'Привет, {name}!\n\n{text} - данная команда мне не известна 😔 введи /start для получения полного списка команд.'

    bot.send_message(
        chat_id=update.effective_message.chat_id,
        text=reply_text,
    )

def main():
    bot = Bot(token=TOKEN,
    )
    updater = Updater(bot=bot,
    )
    
    handler = MessageHandler(Filters.all, message_handler)
    updater.dispatcher.add_handler(handler)

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

