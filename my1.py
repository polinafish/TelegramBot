import telebot
#1918917952:AAEm_uxAr_zzk0EYetYDA0d9F-2hJ1g1VFM

name = ''
surname = ''
age = 0


bot = telebot.TeleBot('1918917952:AAEm_uxAr_zzk0EYetYDA0d9F-2hJ1g1VFM')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")



@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == 'Привет':
        bot.reply_to(message, 'Здравствуй, мой господин')
    elif message.text == '/reg':
        bot.send_message(message.from_user.id, 'Напиши своё имя, пёс!')
        bot.register_next_step_handler(message, reg_name)

def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Говори фамилию, пёс!')
    bot.register_next_step_handler(message, reg_surname)

def reg_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Написал сюда возраст, пёс!')
    bot.register_next_step_handler(message, reg_age)

def reg_age(message):
    global age
    #age = message.text
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Пиши цифрами, пёс!')
    bot.register_next_step_handler(message, reg_ok)

def reg_ok(message):
    bot.send_message(message.from_user.id, 'Тебе ' + str(age) + ' лет? И тебя зовут' + name + ' ' + surname +
                      '? Отвечай, пёс!')


bot.polling()