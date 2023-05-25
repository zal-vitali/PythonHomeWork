# ## Задача 3. 
# Добавьте в telegram-бота игру «Угадай числа». Бот загадывает число от 1 до 1000. 
# Когда игрок угадывает его, бот выводит количество сделанных ходов.

import telebot
import random

secret_number = 0
its_game = False
iter_number = 0

def get_token():
    with open("C:\_token.txt", "r",encoding='utf-8') as file:
        token = file.read()
        return token

def its_int(text):
    try:
        i = int(text)
    except:
        return False
    return True

bot = telebot.TeleBot(get_token())

@bot.message_handler(commands=['start'])
def start_game(message):
    global its_game
    global secret_number
    its_game = True
    secret_number = random.randint(1,1000)
    bot.reply_to(message, "Я загадал число. Угадывай! Чтобы остановить игру введи /stop")

@bot.message_handler(commands=['stop'])
def stop_game(message):
    global its_game
    global secret_number
    global iter_number
    its_game = False
    secret_number = 0
    iter_number = 0
    bot.reply_to(message, "Игра остановлена!")


@bot.message_handler(content_types=['text'])
def game(message):
     global iter_number
     global secret_number
     global its_game
     text = message.text
     if its_game:
        if its_int(text):
            current_number = int(text)
            iter_number = iter_number + 1
            if current_number > secret_number:
                bot.reply_to(message, 'Моё число меньше')
            elif current_number < secret_number:
                bot.reply_to(message, 'Моё число больше')
            else:
                its_game = False
                bot.reply_to(message, f'Молодец, справился! количество твоих ходов - {iter_number}')
        else:
            bot.reply_to(message, 'Соберись, тряпка! Вводи числа!')
bot.polling()    