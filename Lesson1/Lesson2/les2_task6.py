import random

n = 10
prize = random.randint(0, 100)
print(f'число {prize}')
while n > 0:
    bet = int(input('Введите число от 0 да 100: '))
    if bet == prize:
        print(f'Поздравляю вы угадали число {bet}')
        exit(0)
    elif bet > prize:
        print(f'Ваше число больше загаданого')
    else:
        print(f'Ваше число меньше загаданого')
    n -= 1
print(f'Вы проиграли. Было загадано {prize}')
