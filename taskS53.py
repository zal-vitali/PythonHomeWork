# ## Задача 3. 
# Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов есть в списке. 
# Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают Список уникальных элементов 
# [1, 4, 2, 3, 6, 7]

import random

def task():
    n = 10
    numbers = [random.randint(1,10) for _ in range(n)]
    numbersUnique = list(set(numbers))
    print(f'{numbers} => {n - len(numbersUnique)} элемента совпадают. Уникальные: {numbersUnique}')
       

task()