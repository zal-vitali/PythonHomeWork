# ## Задача 3. 
# Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.

import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def decimals():

    for i in range(1,11):
        for j in range(i,12):
            if math.gcd(j, i) == 1 and i/j != 1:
                print(f'{i}/{j}')

decimals()