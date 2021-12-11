import telebot
import random
import sqlite3
from telebot import types
bot = telebot.TeleBot('5081646594:AAEgCAW2FEWM_hyzGuKQBzxbKqNXFmbGFEw')

conn = sqlite3.connect('db/db.db', check_same_thread=False)
cursor = conn.cursor()


happy_list = [
    "Ты самая сладенькая конфеточка.",
    "Ты самый нежный персичек.",
    "Ты самый прелесный цветочек."]

sad_list = [
    "Хуй собачий.",
    "Жир поросячий.",
    "Ммм, хуета."]


def get_buttons(message):
    bot.send_message(message.from_user.id, "Это игра Сладость или Гадость.")
    keyboard = types.InlineKeyboardMarkup()
    key_happy = types.InlineKeyboardButton(text='Сладость', callback_data='happy')
    keyboard.add(key_happy)
    key_sad = types.InlineKeyboardButton(text='Гадость', callback_data='sad')
    keyboard.add(key_sad)
    bot.send_message(message.from_user.id, text='Выбери "Сладость" или "Гадость"', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Хэй":
        get_buttons(message)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши 'Хэй'.")


# @bot.callback_query_handler(func=lambda call: True)
# def callback_worker(call):
#     if call.data == "happy":
#         bot.send_message(call.message.chat.id, random.choice(happy_list))
#         get_buttons(call.message)
#     elif call.data == "sad":
#         bot.send_message(call.message.chat.id, random.choice(sad_list))
#         get_buttons(call.message)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "happy":
        bot.send_message(call.message.chat.id, random.choice(happy_list))
        get_buttons(call.message)
    elif call.data == "sad":
        bot.send_message(call.message.chat.id, random.choice(sad_list))
        get_buttons(call.message)

bot.polling(none_stop=True, interval=0)
