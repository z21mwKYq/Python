# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

a = [random.randint(-5, 10) for _ in range(6)]

print(f'Сгенерированный массив {a}')
Maxind = 0
Minind = 0
smax = a[0]
smin = a[0]
for ind, i in enumerate(a):
    if smax < i:
        smax = i
        Maxind = ind
    if smin > i:
        smin = i
        Minind = ind
print(f'Макс. элемент в массиве {smax} номер {Maxind}')
print(f'Мин. элемент в массиве {smin} номер {Minind}')

del a[Maxind]
a.insert(Maxind, smin)
del a[Minind]
a.insert(Minind, smax)
print(f'Измененный массив {a}')
