# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

S = 0
t = 0
k = 0
while True:
    number = int(input('Введите число, для окончания укажите 0: '))
    if number == 0:
        break
    else:
        k = number
        while number > 0:
            t += number%10
            number //=10
        if S < t:
            S = t
            else
        t = 0
print(f'Число с максимальной суммой цифр {S}')