# Задан массив из случайных цифр на 15 элементов. 
# На вход подаётся трёхзначное натуральное число. 
# Напишите программу, которая определяет, есть в массиве последовательность из трёх элементов, 
# совпадающая с введённым числом.
# [0, 5, 6, 2, 7, 7, 8, 1, 1, 9] - 277 -> да
# [4, 4, 3, 6, 7, 0, 8, 5, 1, 2] - 812 -> нет

import random

def generateList():
    return [random.randint(0,10) for _ in range(15)]

def findSub(list,subSeq):
    stringList = ''.join(map(str, list))
    return(subSeq in stringList)
 
list = generateList()
print(list) 
subSeq = input('Введите число для поиска: ')
print(findSub(list,subSeq))
