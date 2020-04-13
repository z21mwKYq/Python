# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import randint
num = int(input('Введите кол-во строк у квадратной матриц '))
matrix = [[randint(1,100) for _ in range(num)] for _ in range(num)]
Min = matrix[0][0]
Max = 0
m=[]
for line in matrix:
    for item in line:
        print(f'{item:<4}', end='')
    print()

for j in range(len(matrix[0])):
    for i in range(len(matrix)):
        if matrix[i][j] < Min:
            Min = matrix[i][j]
    m.append(Min)
    Min = 150
print (f'Минимальные элементы в столбцах матрицы {m}')

for k in m:
    if Max < k:
        Max = k
print(f'максимальный элемент среди минимальных элементов столбцов матрицы {Max}')
