# ## Задача 2. 
# Создайте двумерный массив, размером 5х5. Определите, есть ли в нём одинаковые строки.
import numpy as np

def array_str():

    size = (5,5)
    numbers = np.random.randint(10, 12, size)
    print(numbers)
    unique_list,counts = np.unique(numbers, return_counts=True, axis=0)
    # print(unique_list)
    # print(counts)

    len_list = len(list(filter(lambda x: x > 1, list(counts))))
    if len_list > 0:
        print('Одинаковые строки есть')
    else:
        print('Одинаковых строк нет')

array_str()