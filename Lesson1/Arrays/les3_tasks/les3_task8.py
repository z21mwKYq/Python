a = []
S = 0
for i in range(0, 4):
    a.append([])
    for k in range(0, 4):
        a[i].append(int(input(f'Элемент {k + 1} стороки {i + 1}: ')))
        S += a[i][k]
    a[i].append(S)
    S = 0

# for r in a:
#     print(f'{r:4} ')

for line in a:
    for item in line:
        print(f'{item:>4}', end='')
    print()
