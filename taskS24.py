# ## Задача 4. 
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]

def createList(number):
    return list(range(-abs(number),abs(number) + 1))

def shiftList(list):
    part1 = list[:len(list)-2]
    part2 = list[len(list)-2:]
    return part2 + part1

print("Задайте список от -N до N. Укажите N: ")
list = createList(int(input()))
print(list)
print(shiftList(list))