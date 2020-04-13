# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

import random
size = int(input(f'Введите размер массива '))
a = [random.randint(1, size*2) for _ in range(size)]
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
