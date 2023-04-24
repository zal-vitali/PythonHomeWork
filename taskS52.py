# ## Задача 2. 
# Дан список случайных чисел. Создайте список, в который попадают числа, 
# описывающие случайную возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [2, 7] или [4, 6, 7] и т.д.

import random

def subsequence(number, list):
    temp = number
    sublist = [number]
    for el in list:
        if el > temp:
            temp = el
            sublist.append(el)
    if len(sublist) > 1:
        print(sublist)

def task():
    numbers = [random.randint(1,10) for _ in range(10)]  
    print(numbers)
    for i in range(len(numbers)-1):
        subsequence(numbers[i], numbers[(i+1):])

task()