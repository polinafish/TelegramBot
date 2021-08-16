import telebot


name = ''
surname = ''
age = 0

retryCount = 0
maxRetryCount = 5


bot = telebot.TeleBot('***')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")



@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == 'Привет':
        bot.reply_to(message, 'Здравствуй, мой господин')
    elif message.text == '/reg':
        retryCount = 0
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
    bot.register_next_step_handler(message, reg_age, 0)

def reg_age(message, retryCount):
    global age
    #age = message.text
    if retryCount < maxRetryCount:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Пиши цифрами, пёс!')
            retryCount = retryCount + 1
            bot.register_next_step_handler(message, reg_age, retryCount)
    if retryCount >= 5:
        bot.send_message(message.from_user.id, 'Ну ты и тупой, говорил же цифрами пиши, пес!')
        bot.clear_step_handler_by_chat_id(message.from_user.id)

    if age != 0:
        reg_ok(message)

def reg_ok(message):
    bot.send_message(message.from_user.id, 'Тебе ' + str(age) + ' лет? И тебя зовут' + name + ' ' + surname +
                      '? Отвечай, пёс!')


bot.polling()
