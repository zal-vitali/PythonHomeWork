# ## Задача 3. 
# Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.

import math

def decimals():

    for i in range(1,11):
        for j in range(i,12):
            #if j % i != 0:
            if math.gcd(j, i) == 1 and i != 1:
                print(f'{i}/{j}')

decimals()