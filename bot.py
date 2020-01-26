#Must be installed python-telegram-bot lib.
from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters
import os

#TOKEN = os.environ.get('serge_kretov_tel_bot') #bot token from @botFather in config vars on heroku.com

TOKEN = '862029754:AAFEch9ivNBD7i82E0TsS0DWhGw0DO0GM8c'

def message_handler(bot:Bot, update:Update):
    user = update.effective_user
    if user:
        name = user.first_name
    else:
        name = 'аноним'

    text = update.effective_message.text
    reply_text = f'Привет, {name}!\n\n{text}'

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

    Updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

