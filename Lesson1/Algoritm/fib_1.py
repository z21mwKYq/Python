import cProfile
import functools

def test_fib(func):
    lst = [0,1,1,2,3,5,8,13,21,34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')
@functools.lru_cache()
def fib(n):
    if n < 2:
        return n
    return fib(n-1)+fib(n-2)
cProfile.run('fib(20)')
# test_fib(fib)

# "fib_1.fib(10)"
# 1000 loops, best of 5: 49.3 usec per loop

#  "fib_1.fib(15)"
# 1000 loops, best of 5: 546 usec per loop

# "fib_1.fib(20)"
# 1000 loops, best of 5: 6.14 msec per loop

# "fib_1.fib(25)"
# 1000 loops, best of 5: 69.2 msec per loop

# --------------------------------------------------------
# 177/1    0.000    0.000    0.000    0.000 fib_1.py:8(fib)

# 1973/1    0.001    0.000    0.001    0.001 fib_1.py:8(fib)

# 21891/1    0.015    0.000    0.015    0.015 fib_1.py:8(fib)
