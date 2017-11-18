#!/usr/bin/env python
import config
import telebot
from telebot.types import (
    ReplyKeyboardMarkup,
    ReplyKeyboardHide,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from status import Status

import db
import places

change_category = "⬅️ Изменить категорию"
send_geo = "🌍 Отправить местоположение"
contact_us = "📣 Связаться с нами"
class Category:
    def __init__(self, name, identificator, number, button_title):
        self.number = number
        self.name = name
        self.button_title = button_title
        self.identificator = identificator

class Categories:

    def __init__(self):
        self.categories_array = []
        self.max_number = 0

    def __iter__(self):
        return iter(self.categories_array)

    def add(self, name, identificator, button_title):
        self.max_number += 1
        self.categories_array.append(
            Category(
                name,
                identificator,
                self.max_number,
                button_title
            )
        )

    def get_elem_by_name(self,name):
        for category in self.categories_array:
            if category.name.lower() == name.lower():
                return category
        return None
    def get_elem_by_buttitle(self, name):
        for category in self.categories_array:
            if category.button_title.lower() == name.lower():
                return category
        return None

categories = Categories()
categories.add(
    name = 'Кафе',
    identificator = 'cafe',
    button_title = '🍽  Кафе'
)
categories.add(
    name = 'Салон Красоты',
    identificator = 'beauty',
    button_title = '💅 Салон Красоты'
)
categories.add(
    name = 'Развлечения',
    identificator = 'party',
    button_title = '🎡 Развлечения'
)

db_interface = db.DBInterface()
bot_token = config.bot_token
bot = telebot.TeleBot(bot_token)

def log_raw_message(message):
    db_interface.log_message(
        message.chat.id,
        message.text,
        message.date,
        message.chat.first_name,
        message.chat.last_name,
        message.chat.username
    )

def log_location(message):
    db_interface.log_message(
        message.chat.id,
        str(message.location.latitude) + ", " + str(message.location.longitude),
        message.date,
        message.chat.first_name,
        message.chat.last_name,
        message.chat.username
    )

def undefined_error(message):
    bot.send_message(
        message.chat.id,
        '🤷 Не понял тебя. Давай попробуем ещё раз'
    )
    greetings(message)
def get_location(message, choose):
    keyboard = ReplyKeyboardMarkup(
        row_width=1,
        resize_keyboard=True,
        one_time_keyboard=True
    )
    button_geo = KeyboardButton(
        text= send_geo,
        request_location=True
    )
    button_change_category = KeyboardButton(
        text=change_category
    )

    keyboard.add(button_geo)
    keyboard.add(button_change_category)
    bot.send_message(
        message.chat.id,
        ('Отлично!\nТы выбрал *{}*.'.format(choose.lower())),
        parse_mode = 'Markdown'
    )
    bot.send_message(
        message.chat.id,
        (
        'Теперь дай мне знать, где ты, чтобы я мог' +
        ' подобрать для тебя лучшее заведение!'
        ),
        reply_markup=keyboard

    )

def send_contact_info(message):
    bot.send_message(
        message.chat.id,
        ("📢 Ты можешь в любой момент связаться с нами:\n" +
        "☎️ по телефону: [+79166498288](tel+791664982887)\n" +
        "📧 по почте: gaidukov.artem@me.com\n\n"
        ),
        parse_mode="Markdown"
    )
    bot.send_message(
        message.chat.id,
        ("Мы любим общаться с нашими пользователями!" +
        "Обращайтесь с любыми отзывами и предложениями! 😉"
        ),
        parse_mode="Markdown"
    )
@bot.message_handler(content_types=["location"])
def location_recieved(message):

    status = db_interface.get_status(message.chat.id)
    log_location(message)

    if not Status.was_choosed_smth(status):
        bot.send_message(
            message.chat.id,
            "Я узнаю, где ты, позже"
        )
        return

    bot.send_message(
        message.chat.id,
        "Лучшие места для тебя:",
        reply_markup=ReplyKeyboardHide()
    )
    db_interface.set_status(
        message.chat.id,
        Status.choosed_to_geo(status)
    )

    places_list = places.get_top_of_places(status, message.location)
    for place in places_list:
        keyboard = InlineKeyboardMarkup()
        callback_button = InlineKeyboardButton(
            text="👍 Интересно!",
            callback_data="place_{}".format(place[0])
        )
        keyboard.add(callback_button)
        for m in place[1][:-1]:
            bot.send_message(
                message.chat.id,
                m,
                parse_mode = 'Markdown'
            )
        bot.send_message(
            message.chat.id,
            place[1][-1],
            reply_markup=keyboard,
            parse_mode = 'Markdown'
        )

    keyboard = ReplyKeyboardMarkup(
        row_width=1,
        resize_keyboard=True,
        one_time_keyboard=True
    )
    button_change_category = KeyboardButton(
        text=change_category
    )

    keyboard.add(button_change_category)
    bot.send_message(
        message.chat.id,
        (
        'Если ничего из предложенного не нравится, можешь перейти назад ' +
        'и выбрать другую категорию'
        ),
        reply_markup=keyboard

    )

@bot.message_handler(commands=["start"])
def greetings(message, dont_log=False):
    if not dont_log:
        log_raw_message(message)

    db_interface.set_status(
        message.chat.id,
        Status.just_started
    )
    send_contact_info(message)
    markup = telebot.types.ReplyKeyboardMarkup(
        one_time_keyboard=True,
        resize_keyboard=True
    )
    for c in categories:
        markup.add(c.button_title)

    bot.send_message(message.chat.id,
        "Что ты хочешь посетить?",
        reply_markup=markup
    )

@bot.message_handler(content_types=["text"])
def talk(message):
    log_raw_message(message)
    status = db_interface.get_status(message.chat.id) 
    if message.text == contact_us:
        send_contact_info(message)
        return
    if status == Status.just_started:
        if message.text.strip().lower() == 'бордель':
            bot.send_message(
                message.chat.id,
                '👿 А ты зубки почистил, маленький негодяй?'
            )
            return
        category = categories.get_elem_by_buttitle(message.text)
        if category is not None:
            db_interface.set_status(
                message.chat.id,
                Status.create_choosed_status(category.identificator)
            )
            get_location(message, category.name)
        else:
            undefined_error(message)
    elif (Status.was_choosed_smth(status) or
        Status.was_sent_geo(status)):
        if message.text == change_category:
            db_interface.set_status(
                message.chat.id,
                Status.just_started
            )
            greetings(message)
        else:
            undefined_error(message)


@bot.callback_query_handler(func=lambda call: True)
def choose_place(call):
    if call.message:
        if call.data.startswith("place"):
            place_id = call.data.split('_')[1]
            place_info = db_interface.get_place_by_id(place_id)

            bot.send_message(
                call.message.chat.id,
                "Отлично!\nЗаходи в *{}*".format(place_info[1]),
                reply_markup=ReplyKeyboardHide(),
                parse_mode="Markdown"
            )

            keyboard = InlineKeyboardMarkup()
            callback_button = InlineKeyboardButton(
                text="⬅️ В начало",
                callback_data="start"
            )
            keyboard.add(callback_button)
            bot.send_message(
                call.message.chat.id,
                "По адресу _{}_".format(place_info[5]),
                reply_markup=keyboard,
                parse_mode="Markdown"
            )
        elif call.data == 'start':
            greetings(call.message, dont_log=True)

if __name__ == '__main__':
    bot.polling(none_stop=True)
