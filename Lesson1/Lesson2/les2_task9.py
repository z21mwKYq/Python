# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

S = 0
t = 0
# num = 0
while True:
    number = int(input('Введите число, для окончания укажите 0: '))
    num = number
    if number == 0:
        break
    else:
        while number > 0:
            t += number % 10
            number //= 10
        if S < t:
            S = t
            nmax = num
        t = 0
print(f'Число с максимальной суммой цифр {nmax}, сумма цифр - {S}')
