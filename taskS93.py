# ## Задача 3. 
# Создайте двумерный массив случайного размера. Найдите индексы максимального и минимального элементов в нём.
# Выведите элементы главной диагонали матрицы в виде одномерного массива.

import numpy as np

def matrix():
    min_size = 3
    max_size = 7
    numbers = np.random.randint(10,100, (np.random.randint(min_size, max_size), np.random.randint(min_size, max_size)))
    print(numbers)

    min_val = np.min(numbers)
    i, j = np.where(numbers == min_val)
    print(f'минимальное значение: {min_val}, индекс: {i}{j}')
    max_val = np.max(numbers)
    i, j = np.where(numbers == max_val)
    print(f'максимальное значение: {max_val}, индекс: {i}{j}')

    print(f'диагональ: {numbers.diagonal()}')

matrix()