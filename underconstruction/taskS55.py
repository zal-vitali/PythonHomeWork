# ## Задача 5*. 
# (Необязательная). Двумерный массив размером 5х5 заполнен 
# случайными нулями и единицами. Игрок может ходить только по 
# полям, заполненным единицами. Проверьте, существует ли путь из точки [0, 0] в точку [4, 4]
# (эти поля требуется принудительно задать равными единице).

import random
matrix = []
dimension = int(5)
goalX = int(4)
goalY = int(4)

def initialiseMatrix():
    for i in range(dimension):
        string = [random.randint(0,1) for _ in range(dimension)]
        matrix.append(string)
        
    return matrix
  
def step(x,y):
    if x == goalX and y == goalY:
        return True
    #elif matrix[x][y] == 2:
    #    return False
    else:        
        if matrix[x][y] == 1:
            matrix[x][y] = 2
            if x < dimension - 1:
               return step(x+1,y)
            elif y < dimension - 1: 
                return step(x,y+1)
            elif x > 0:
                return step(x-1,y)
            elif y > 0:    
                return step(x,y-1)


def task():
    matrix = initialiseMatrix()
    matrix[0][0] = 1
    matrix[goalX][goalY] = 1

    for i in range(dimension):  
        print(matrix[i-1])
    print('------------')

    print(step(0,0)) 

    for i in range(dimension):  
        print(matrix[i-1])

task()