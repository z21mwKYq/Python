# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random
size = int(input(f'Введите размер массива '))
a = [random.randint(1, size) for _ in range(size)]
print(f'Сгенерированный массив {a}')
Min = a[0]
Max = a[0]
S = 0
Tmin = 0
Tmax = 0
for id, i in enumerate(a):
    if i > Max:
        Max = i
        Tmax = id
    if i < Min:
        Min = i
        Tmin = id
# print(f'Минимальный элемент {Min} ,его номер {Tmin} ') #Для проверки
# print(f'Максимальный элемент {Max} ,его номер {Tmax} ') #Для проверки
if Tmin < Tmax:
    for i in a[Tmin + 1: Tmax]:
        S += i
else:
    for i in a[Tmax + 1: Tmin]:
        S += i
print(f'Сумма между минимальным и максимальным элементом равна - {S}')
