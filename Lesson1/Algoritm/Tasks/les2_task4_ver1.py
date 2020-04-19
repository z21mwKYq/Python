# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.
import cProfile
def raw(n, S=1):
    if n <= 0:
        return S
    else:
        return S + raw(n - 1, S / (-2))

cProfile.run("raw(900)")
# n = int(input("Введите кол-во элементов: "))
# if n <= 0:
#     print("Неверное кол-во элементов")
# else:
# print(raw(n-1))

# timeit

# import les2_task4_ver1" "les2_task4_ver1.raw(10)"
# 1000 loops, best of 5: 5.53 usec per loop

# "import les2_task4_ver1" "les2_task4_ver1.raw(100)"
# 1000 loops, best of 5: 54.9 usec per loop

# "import les2_task4_ver1" "les2_task4_ver1.raw(200)"
# 1000 loops, best of 5: 113 usec per loop

# import les2_task4_ver1" "les2_task4_ver1.raw(500)"
# 1000 loops, best of 5: 308 usec per loop

# "import les2_task4_ver1" "les2_task4_ver1.raw(900)"
# 1000 loops, best of 5: 581 usec per loop

# cProfile

# cProfile.run("raw(10)")
# 11/1    0.000    0.000    0.000    0.000 les2_task4_ver1.py:4(raw)

# cProfile.run("raw(100)")
# 101/1    0.000    0.000    0.000    0.000 les2_task4_ver1.py:4(raw)

# cProfile.run("raw(200)")
# 201/1    0.001    0.000    0.001    0.001 les2_task4_ver1.py:4(raw)

# cProfile.run("raw(500)")
# 501/1    0.002    0.000    0.002    0.002 les2_task4_ver1.py:4(raw)


# cProfile.run("raw(900)")
# 901/1    0.003    0.000    0.003    0.003 les2_task4_ver1.py:4(raw)

