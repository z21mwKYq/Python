k = 0
for i in range(32, 128):
    if k > 9:
        print('')
        k = 0
    else:
        k += 1
    print(f'{i:3} - {chr(i)}', end=' | ')
