# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).


num = int(input("Введите натуральное число: "))
odd = 0
even = 0
while num > 0:
    if (num % 10) % 2 != 0:
        odd += 1
    else:
        even += 1
    num //= 10
print(f'Кол-во четных - {even}, кол-во нечетных - {odd}')
