# # Задача 2. 
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

import math

def distance2D(ax,ay,bx,by):
    
    dx2 = math.pow((ax - bx),2)
    dy2 = math.pow((ay - by),2)
    return round(math.sqrt(dx2 + dy2),2)

print('Для нахождения расстояния между точками введите их координаты:')
ax = int(input("A(x):"))
ay = int(input("A(y):"))
bx = int(input("B(x):"))
by = int(input("B(y):"))

print(distance2D(ax,ay,bx,by))