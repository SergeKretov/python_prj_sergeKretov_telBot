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
        txt1 = 'Я виртуальный помощник Сергея Сергеевича из Юридического агентства ПРИОРИТЕТ (г.Норильск).'
        txt2 = 'Наше агентство оказывает следующие услуги:'
        txt3 = '👨🏻‍🎓Консультации по любым правовым вопросам'
        txt4 = '💼Подготовка исков, жалоб, претензий'
        txt5 = '⚖️Участие представителя в Суде'
        txt6 = '💶Банкротство граждан (списание долгов)'
        txt7 = '🏛Арбитражные споры'
        txt8 = '💻Прочие сопутствующие услуги'
        txt9 = 'Введите соответствующую команду для получения интересующей Вас информации:'
        txt10 = '📆Записаться на прием - /запись'
        txt11 = '📚Узнать цены - /цена'
        txt12 = '💸Подробнее о банкротстве - /банкрот'
        txt13 = 'Посетить сайт агентства - /сайт'
        txt14 = '🖥Войти в кабинет клиента - /клиент'
        txt15 = '📰Получить краткую информацию о нас - /инфо'
        txt16 = '📲Написать непосредственно Сергею Сергеевичу - /сергей'
        reply_text = f'Привет, {name}!\n\n{txt1}\n{txt2}\n\n{txt3}\n{txt4}\n{txt5}\n{txt6}\n{txt7}\n{txt8}\n\n{txt9}\n{txt10}\n{txt11}\n{txt12}\n{txt13}\n{txt14}\n{txt15}\n{txt16}'
    
    elif text == '/запись':
        pass
    
    elif text == '/цена':
        pass
    
    elif text == '/банкрот':
        pass
    
    elif text == '/сайт':
        txt17 = 'http://юа-право.рф'
        txt18 = 'http://www.prioritetus.ru'
        reply_text = f'Итак, {name}, для перехода на наш сайт кликни по ссылке {txt17}\n или по ссылке резервного сайта {txt18}'
    
    elif text == '/клиент':
        pass
    
    elif text == '/инфо':
        pass
    
    elif text == '/сергей':
        pass
    
    else:
        reply_text = f'{name},\n\n{text} - данная команда мне не известна 😔 введи /start для получения полного списка команд.'

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

