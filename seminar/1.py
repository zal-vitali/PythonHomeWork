# Задача 1. Дан список случайных элементов.
# Проверьте, что все его элементы уникальны.
# Решение задач:
# [7, 2, 4, 1, 6] –> да
# [7, 2, 4, 2, 6] -> нет

import random

def task1():
    n = 10
    numbers = [random.randint(1,50) for _ in range(n)]
    numbersUnique = list(set(numbers))
    if len(numbers) == len(numbersUnique):
        return True
    return False
#print(unique())

# Задача 2. Даны два случайных пятизначных числа.
# Определить, состоят ли они из одних и тех же цифр.
# 20 мин
# 72426, 27624 –> да
# 44444, 44441 -> нет

def task2():
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

    # Через словарь тоже можно
    # num_f_dict = ([i,number1.count(i)] for i in set(number1))
    # num_f_dict = dict(num_f_dict)
    # print(num_f_dict)

def task3():
    expression = input()
    # if '+' in expression:
    #     a, b = map(float, expression.split('+'))
    #     print(a+b)

    expression = expression.replace('+', '+-')

    if '+' in expression:
        expression = expression.split('+')
        print(int(expression[0]) + int(expression[1]))
    elif '-' in expression:
        expression = expression.split('-')
        print(int(expression[0]) - int(expression[1]))
    elif '*' in expression:
        expression = expression.split('*')
        print(int(expression[0]) * int(expression[1]))
    elif '/' in expression:
        expression = expression.split('/')
        print(int(expression[0]) / int(expression[1]))
    
        #eval(expression)

def task4():

    for i in range(100):
        for j in range(100):
            k = 100 - i - j
            if i*100 + j*50 + k*5 == 1000:
                return [i,j,k]

print(task4())