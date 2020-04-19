import cProfile
def test_fib(func):
    lst = [0,1,1,2,3,5,8,13,21,34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')

def fib_loop (n):
    if n < 2:
        return n
    first,second = 0,1
    for i in range(2,n+1):
        first,second = second , first + second
    return second

# test_fib(fib_loop)

# fib3.fib_loop(10)"
# 1000 loops, best of 5: 2.38 usec per loop

# fib3.fib_loop(15)"
# 1000 loops, best of 5: 3.19 usec per loop

# fib3.fib_loop(20)"
# 1000 loops, best of 5: 4.11 usec per loop

# fib3.fib_loop(100)"
# 1000 loops, best of 5: 16.2 usec per loop

# fib3.fib_loop(200)"
# 1000 loops, best of 5: 33.8 usec per loop

# fib3.fib_loop(500)"
# 1000 loops, best of 5: 94.9 usec per loop

# fib3.fib_loop(1000)"
# 1000 loops, best of 5: 216 usec per loop

# -------------------------------------------
cProfile.run('fib_loop(50000)')

# 4 function calls in 0.000 seconds

# 4 function calls in 0.000 seconds

# 4 function calls in 0.000 seconds

# 4 function calls in 0.000 seconds

# 4 function calls in 0.103 seconds

