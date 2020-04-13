# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random
size = int(input(f'Введите размер массива '))
a = [random.randint(-50, 50) for _ in range(size)]
smax = -100
print(f'Сгенерированный массив {a}')

tmp = [item for item in a if item < 0]
# print(tmp)

for i in tmp:
    if smax < i:
        smax = i
# print(smax)
print(f'Максимальный отрицательный элемент {smax}, его позиция {a.index(smax)}')
