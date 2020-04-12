# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# второй массив надо заполнить значениями 0, 3, 4, 5 (помните, что индексация начинается с нуля),
# т. к. именно в этих позициях первого массива стоят четные числа.

import random

a = [random.randint(1,10) for _ in range(6)]
b = []
print(f'Сгенерированный случайными числами первый массив {a}')

for ind, i in enumerate(a):
    if i % 2 == 0:
      b.append(ind)
print(f'Массив с индексами четных элементов первого массива {b}')