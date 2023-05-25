# ## Задача 2. 
# Напишите программу, которая позволяет считывать из файла вопрос,
# отвечать на него и отправлять ответ обратно пользователю.

import telebot

def get_token():
    with open("C:\_token.txt", "r",encoding='utf-8') as file:
        token = file.read()
        return token

bot = telebot.TeleBot(get_token())

def read_file():
    with open("supportlog.txt", "r",encoding='utf-8') as file:
        data = file.readlines()
        result = []
        for str in data:
            str = str[:-1]
            str_list = str.split(':')
            if len(str_list) == 2:
                answer = input(f'Вопрос: {str_list[1]}\n Ответ: ')
                if answer != '':
                    str = f'{str_list[0]}:{str_list[1]}:{answer}'
                    bot.send_message(str_list[0], f'вы спрашивали, {str_list[1]}')
                    bot.send_message(str_list[0], f'Отвечаем: {answer}')
            result.append(f'{str}\n')

    with open("supportlog.txt", "w",encoding='utf-8') as file:
        file.writelines(result)
read_file()
 

