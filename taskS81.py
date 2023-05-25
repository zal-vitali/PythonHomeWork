# ## Задача 1. 
# Напишите бота для техподдержки. Бот должен записывать обращения пользователей в файл.

import telebot

support_mode = False

def get_token():
    with open("C:\_token.txt", "r",encoding='utf-8') as file:
        token = file.read()
        return token

bot = telebot.TeleBot(get_token())

@bot.message_handler(commands=['support'])
def start_game(message):
    global support_mode
    support_mode = True
    bot.reply_to(message, "Напишите сообщение в поддержку")

@bot.message_handler(content_types=['text'])
def processing_message(message):
    global support_mode
    if support_mode:
        with open("supportlog.txt", "a",encoding='utf-8') as file:
            file.write(f'{message.from_user.id}:{message.text}\n')
        support_mode = False
        bot.reply_to(message, "Спасибо за обращение. Напишите нам, используя команду /support")

bot.polling()        