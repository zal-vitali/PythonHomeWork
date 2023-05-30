# ## Задача 1. 
# Дан список элементов. Используя библиотеку NumPy, подсчитайте количество уникальных элементов в нём.

import numpy as np

def unique_el():
    list = [1,3,4,2,5,3,7,3,4]
    unique_list = np.unique(list)
    print(f'В списке {list} количество уникальных элементов: {len(unique_list)}')
    
unique_el()