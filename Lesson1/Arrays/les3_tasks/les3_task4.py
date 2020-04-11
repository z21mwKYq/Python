# 4. Определить, какое число в массиве встречается чаще всего.
import random
# a = [3,0,3]
a = [random.randint(1, 5) for _ in range(10)]
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

print (imax, Smax)

