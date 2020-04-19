# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.
import cProfile
import functools
# import sys
# sys.setrecursionlimit(1500)
@functools.lru_cache()
def raw(n, S=1):
    if n <= 0:
        return S
    else:
        return S + raw(n - 1, S / (-2))
cProfile.run('raw(200)')
# timeit
# "import les2_task4_ver3" "les2_task4_ver3.raw(10)"
# 1000 loops, best of 5: 283 nsec per loop

# "import les2_task4_ver3" "les2_task4_ver3.raw(100)"
# 1000 loops, best of 5: 287 nsec per loop

# "import les2_task4_ver3" "les2_task4_ver3.raw(200)"
# 1000 loops, best of 5: 270 nsec per loop

# cProfile

# cProfile.run('raw(10)')
# 11/1    0.000    0.000    0.000    0.000 les2_task4_ver3.py:5(raw)
# cProfile.run('raw(100)')
# 101/1    0.000    0.000    0.000    0.000 les2_task4_ver3.py:5(raw)
# cProfile.run('raw(200)')
# 201/1    0.001    0.000    0.001    0.001 les2_task4_ver3.py:5(raw)
