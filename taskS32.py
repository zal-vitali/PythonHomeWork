# ## Задача 2. 
# В списке находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.

def fruitsList():
    with open("fruits.txt", "r",encoding='utf8') as file:
        return file.read().splitlines()

def separateFruits(letter):
    separateList = []
    list = fruitsList()
    for el in list:
        if el[0] == letter:
            separateList.append(el)
    return(separateList)

letter = input('Укажите начальную букву фрукта: ')
print(separateFruits(letter))


