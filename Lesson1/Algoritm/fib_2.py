import cProfile
def test_fib(func):
    lst = [0,1,1,2,3,5,8,13,21,34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')

def fib_dict(n):
    fib_d = {0:0 , 1:1}
    def _fib_dict(n):
        if n in fib_d:
            return fib_d[n]
        fib_d[n] = _fib_dict(n-1)+_fib_dict(n-2)
        return fib_d[n]
    return _fib_dict(n)
# test_fib(fib_dict)

# "fib_2.fib_dict(10)"
# 1000 loops, best of 5: 13 usec per loop

# "fib_2.fib_dict(15)"
# 1000 loops, best of 5: 18.9 usec per loop

# fib_2.fib_dict(20)"
# 1000 loops, best of 5: 24.8 usec per loop

# fib_2.fib_dict(25)"
# 1000 loops, best of 5: 32 usec per loop

# fib_2.fib_dict(100)"
# 1000 loops, best of 5: 131 usec per loop

# fib_2.fib_dict(200)"
# 1000 loops, best of 5: 252 usec per loop

# fib_2.fib_dict(500)"
# 1000 loops, best of 5: 734 usec per loop

# -------------------------------------------------------------
cProfile.run("fib_dict(500)")

# 33 function calls (5 primitive calls) in 0.000 seconds
# 43 function calls (5 primitive calls) in 0.000 seconds
# 203 function calls (5 primitive calls) in 0.000 seconds
# 403 function calls (5 primitive calls) in 0.001 seconds
# 1003 function calls (5 primitive calls) in 0.003 seconds
