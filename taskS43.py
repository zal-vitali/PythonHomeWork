# ## Задача 3. 
# Выведите число π с заданной точностью. Точность выводится в виде десятичной дроби.

import math

def accuracy(num):
    pi  = math.pi
    return round(pi, num)
    #return(((pi*10**num)//1)/10**num)

print(accuracy(5))