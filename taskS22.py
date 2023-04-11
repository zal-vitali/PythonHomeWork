## Задача 2. 
#Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.

def logical():
    print('X|Y|Z|Value')
    for x in range(0,2):
        for y in range(0,2):
            for z in range(0,2):
                print(f'{x}|{y}|{z}|{bool(not (x or y) and z)}')

logical()