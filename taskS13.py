# # Задача 3. 
# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).
# 1 -> x > 0, y > 0

def possCoord(number):
    if number == 1:
        return 'x > 0, y > 0'
    elif number == 2:
         return 'x < 0, y > 0'   
    elif number == 3:
         return 'x < 0, y < 0' 
    elif number == 4:
         return 'x > 0, y < 0'
    else: 
        return 'null'    

quarter = int(input('Введите номер четверти: '))
print(f'Доступные коррдинаты для четверти {quarter}: {possCoord(quarter)}')