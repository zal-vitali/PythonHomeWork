# # ## Задача 3. 
# # Создайте скрипт бота, который находит ответы на фразы
# # по ключу в словаре. Бот должен, как минимум, отвечать 
# # на фразы «привет», «как тебя зовут». Если фраза ему 
# # неизвестна, он выводит соответствующую фразу.

dictionnary = dict()

def initialiseBot():
    with open("bot.txt", "r",encoding='utf8') as file:
        return listToDict(file.read().splitlines())

def writeBot(key, value):
    with open("bot.txt", "a",encoding='utf8') as file:
        instring = '\n' + key + '#' + value
        file.write(instring)

def listToDict(list):
    for el in list:
        keyAndValue = el.split('#')     
        dictionnary[keyAndValue[0]] = keyAndValue[1]

# def dictToList(dict):
#     tempList = [f'{key}#{value}' for key, value in dict.items()]
#     writeBot(tempList)

def dialogue():
    print('Привет! Я - бот. Давай пообщаемся!')
    if input().lower() == 'давай':
        initialiseBot()
        flag = True
        while flag:
            if input().lower() == 'пока':
                print('Пока!')
                flag = False  
            else:
                message = input().lower()
                if message in dictionnary:
                    print(dictionnary[message]) 
                else:
                    print('как ответить?')
                    answer = input()
                    dictionnary[message] = answer
                    writeBot(message,answer)       

dialogue() 