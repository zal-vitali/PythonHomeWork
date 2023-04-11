# # Задача 4. 
# Напишите программу, которая на вход принимает число (N), 
# а на выходе показывает все чётные числа от 1 до N.
# 5 -> 2, 4
# 8 -> 2, 4, 6, 8

def evenNumbers(number):
    
    evenNumbers = []
    for i in range(2,number+1,2):
        evenNumbers.append(i)
    return evenNumbers

print('Для нахождения всех чётных чисел от 1 до N, введите значение N:')
number = int(input("N="))


print(evenNumbers(number))