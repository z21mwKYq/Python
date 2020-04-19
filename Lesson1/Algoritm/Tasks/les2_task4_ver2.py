# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.
import cProfile


def raw_loop(n):
    S = 1
    summ = 1
    for i in range(1, n):
        if n == 1:
            summ = 1
            continue
        S = S / (-2)
        summ += S
    return summ


cProfile.run('raw_loop(2000)')

# print(raw_loop(100))

# timeit

# "les2_task4_ver2.raw_loop(10)"
# 1000 loops, best of 5: 4.87 usec per loop

# "import les2_task4_ver2" "les2_task4_ver2.raw_loop(100)"
# 1000 loops, best of 5: 32.3 usec per loop

# "les2_task4_ver2.raw_loop(200)"
# 1000 loops, best of 5: 67.5 usec per loop

# "import les2_task4_ver2" "les2_task4_ver2.raw_loop(500)"
# 1000 loops, best of 5: 163 usec per loop

# "import les2_task4_ver2" "les2_task4_ver2.raw_loop(900)"
# 1000 loops, best of 5: 314 usec per loop

# "import les2_task4_ver2" "les2_task4_ver2.raw_loop(2000)"
# 1000 loops, best of 5: 692 usec per loop

# cProfile

# cProfile.run('raw_loop(10)')
# 1    0.000    0.000    0.000    0.000 les2_task4_ver2.py:6(raw_loop)

# cProfile.run('raw_loop(100)')
# 1    0.000    0.000    0.000    0.000 les2_task4_ver2.py:6(raw_loop)

# cProfile.run('raw_loop(200)')
# 1    0.000    0.000    0.000    0.000 les2_task4_ver2.py:6(raw_loop)

# cProfile.run('raw_loop(500)')
# 1    0.000    0.000    0.000    0.000 les2_task4_ver2.py:6(raw_loop)

# cProfile.run('raw_loop(900)')
# 1    0.000    0.000    0.000    0.000 les2_task4_ver2.py:6(raw_loop)

# cProfile.run('raw_loop(2000)')
# 1    0.000    0.000    0.000    0.000 les2_task4_ver2.py:6(raw_loop)
