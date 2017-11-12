#!/usr/bin/env python
import config
import telebot
from status import Status

import db
import places

class Category:
    def __init__(self, name, identificator):
        self.name = name
        self.identificator = identificator
categories = [
    Category(
        name='Кафе',
        identificator='cafe'
    ),
    Category(
        name='Салон Красоты',
        identificator='beauty'
    ),
    Category(
        name='Развлечение',
        identificator='party'
    )
]

db_interface = db.DBInterface()
bot_token = config.bot_token
bot = telebot.TeleBot(bot_token)
def log_raw_message(message):
    db_interface.log_message(
        message.chat.id,
        message.text,
        message.date
    )
def log_location(message):
    db_interface.log_message(
        message.chat.id,
        str(message.location.latitude) + ", " + str(message.location.longitude),
        message.date
    )

def undefined_error(message):
    bot.send_message(
        message.chat.id,
        'Не понял тебя. Давай попробуем ещё раз'
    )
    greetings(message)
def get_location(message, choose):
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    button_geo = telebot.types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_geo)
    bot.send_message(
        message.chat.id,
        'Отлично! Ты выбрал ' + choose.lower() + '. Теперь дай мне знать, где ты, чтобы я мог подобрать для тебя лучшее заведение!',
    reply_markup=keyboard
    )

@bot.message_handler(content_types=["location"])
def location_recieved(message):
    def choosed_to_geo(choosed):
        if choosed == Status.cafe_choosed:
            return Status.geo_cafe
        elif choosed == Status.beauty_choosed:
            return Status.geo_beauty
        elif choosed == Status.party_choosed:
            return Status.geo_party
        else:
            return Status.just_started

    status = db_interface.get_status(message.chat.id)
    log_location(message)
    if status in (
        Status.cafe_choosed,
        Status.beauty_choosed,
        Status.party_choosed
    ):
        bot.send_message(
            message.chat.id,
            "Лучшие места для тебя:",
            reply_markup=telebot.types.ReplyKeyboardHide()
        )
        db_interface.set_status(
            message.chat.id,
            choosed_to_geo(status))
        places_list = places.get_top_of_places(status, message.location)
        for place in places_list:
            keyboard = telebot.types.InlineKeyboardMarkup()
            callback_button = telebot.types.InlineKeyboardButton(text="Интересно!", callback_data="place_{}".format(place[0]))
            keyboard.add(callback_button)
            bot.send_message(
                message.chat.id,
                place[1],
                reply_markup=keyboard
            )
    else:
        bot.send_message(
            message.chat.id,
            "Я узнаю, где ты, позже"
        )

@bot.message_handler(commands=["start"])
def greetings(message, dont_log=False):
    if not dont_log:
        log_raw_message(message)
    db_interface.set_status(
        message.chat.id,
        Status.just_started
    )
    markup = telebot.types.ReplyKeyboardMarkup(
        one_time_keyboard=True,
        resize_keyboard=True
    )
    for c in categories:
        markup.add(c.name)

    bot.send_message(message.chat.id,
        "Что ты хочешь посетить?",
        reply_markup=markup
    )

@bot.message_handler(content_types=["text"])
def talk(message):
    log_raw_message(message)
    status = db_interface.get_status(message.chat.id) 
    if (status == Status.just_started):
        if message.text == categories[0].name:
            db_interface.set_status(
                message.chat.id,
                Status.cafe_choosed
            )
            get_location(message, 'кафе')
        elif message.text == categories[1].name:
            db_interface.set_status(
                message.chat.id,
                Status.beauty_choosed
            )
            get_location(message, 'салон красоты')
        elif message.text == categories[2].name:
            db_interface.set_status(
                message.chat.id,
                Status.party_choosed
            )
            get_location(message, 'Развлечение')
        else:
            undefined_error(message)

@bot.callback_query_handler(func=lambda call: True)
def choose_place(call):
    if call.message:
        if call.data.startswith("place"):
            place_id = call.data.split('_')[1]
            place_info = db_interface.get_place_by_id(place_id)
            keyboard = telebot.types.InlineKeyboardMarkup()
            callback_button = telebot.types.InlineKeyboardButton(text="В начало", callback_data="start")
            keyboard.add(callback_button)

            bot.send_message(
                call.message.chat.id,
                ("Отлично! Заходи в {} по адресу:\n" +
                " {}").format(place_info[1], place_info[5]),
                reply_markup=keyboard
            )
        elif call.data == 'start':
            greetings(call.message, dont_log=True)

if __name__ == '__main__':
    bot.polling(none_stop=True)
