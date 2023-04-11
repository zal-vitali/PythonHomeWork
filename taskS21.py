# ## Задача 1. 
# Напишите программу, которая принимает на вход число N 
# и выдает список факториалов для чисел от 1 до N.
# пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def factorial(number):
    if number < 2:
        return 1
    else:
        return number * factorial(number-1)   

def fList(number):
    
    factorials = []
    for i in range(1,number+1):
        factorials.append(factorial(i))
    return factorials

print('Для вывода всех факториалов от 1 до N, введите значение N:')
number = int(input("N="))

print(f'N = {number} -> {fList(number)}')