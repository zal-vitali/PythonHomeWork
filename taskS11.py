# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и выводит название этого дня недели.
# 1 –> Понедельник
# 10 –> Нет такого дня
# 7 –> Воскресение

def weekDay(number):
    if number == 1:
        return 'Понедельник'
    elif number == 2:
         return 'Вторник'   
    elif number == 3:
         return 'Среда' 
    elif number == 4:
         return 'Четверг' 
    elif number == 5:
         return 'Пятница' 
    elif number == 6:
         return 'Суббота'
    elif number == 7:
         return 'Воскресение'       
    else:
        return 'Нет такого дня'    

numberDay = int(input('Введите номер дня недели: '))
print(f'День недели с номером {numberDay} - {weekDay(numberDay)}')