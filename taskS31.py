## Задача 1. 
# Создайте список. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8

def f(n):
    if n < 3:
        return 1
    else:
        return f(n - 1) + f(n - 2)    

n = int(input('Введите число для вывода последовательности Фибоначчи: '))

list = [f(i) for i in range(1, n + 1)]
print(list)