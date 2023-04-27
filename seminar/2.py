# Задача 2. Даны два случайных пятизначных числа.
# Определить, состоят ли они из одних и тех же цифр.
# 20 мин
# 72426, 27624 –> да
# 44444, 44441 -> нет

def task():
    number1 = input('N1 ')
    number2 = input('N2 ')

    #set1 = {number1[i] for i in range(int(number1)-1)}
    #set2 = {number2[i] for i in range(int(number2)-1)}
    #set1 = set(list(number1))
    #set2 = set(list(number2))
    #print(set1)
    #print(set2)
    list1 = sorted(list(number1))
    list2 = sorted(list(number2))
    print(list1)
    print(list2)
    #print(set1 == set2)
    print(list1 == list2)

task()    
