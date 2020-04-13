# 4. Определить, какое число в массиве встречается чаще всего.
import random
size = int(input(f'Введите размер массива '))
a = [random.randint(1, size//2) for _ in range(size)]
print(f'Сгенерированный массив {a}')
Smax = 0
Max = 0
imax = 0

for i in a:
    for k in a:
        if i == k:
            Max += 1
    if Smax < Max-1:
        Smax = Max
        imax = i
    Max = 0

print (f'Чаще всего встречается число {imax}, оно встречается {Smax} раз')

