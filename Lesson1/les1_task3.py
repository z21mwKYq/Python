#  Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
#  Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
#  Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
import random
a1 = int(input('Введите первое целое число: '))
a2 = int(input('Введите второе целое число: '))
a = int(random.randint(a1, a2))
b1 = float(input('Введите первое вещ. число: '))
b2 = float(input('Введите второе вещ. число: '))
b = random.random() * (b2 - b1) + b1
c1 = ord(input('Введите первый символ: ').lower())
c2 = ord(input('Введите второй символ: ').lower())
c = int(random.randint(c1,c2))
print(f'Случайное целое число: {a}')
print(f'Случайное вещ. число: {b}')
print(f'Случайный символ: {chr(c)}')
