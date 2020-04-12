# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

import random

a = [random.randint(1, 20) for _ in range(10)]
print(f'Сгенерированный массив {a}')

n = 2
S = []

while n > 0:
    Min = a[0]
    Tid = 0
    for id, i in enumerate(a):
        if Min > i:
            Min = i
            Tid = id
    S.append(a.pop(Tid))
    n -= 1
print(f'Два минимальных элемента {S}')
