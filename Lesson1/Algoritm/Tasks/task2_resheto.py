import cProfile
def fun_sieve (num):
    n = 1
    while True:
        sieve = [i for i in range(n+1)]
        sieve[1] = 0
        for i in range(2,n+1):
            if sieve[i] !=0:
                j = i*2
                while j < n+1:
                    sieve[j] = 0
                    j += i
        result = [i for i in sieve if i !=0]
        if len(result) == num:
            break
        n += 1
    return result[-1]
cProfile.run('fun_sieve(200)')
# print (fun_sieve(1))

# timeit

"task2_resheto.fun_sieve(10)"
# 1000 loops, best of 5: 425 usec per loop

# "task2_resheto.fun_sieve(100)"
# 1000 loops, best of 5: 149 msec per loop

# cProfile
# cProfile.run('fun_sieve(10)')
# 91 function calls in 0.001 seconds

# cProfile.run('fun_sieve(100)')
# 1627 function calls in 0.153 seconds

# cProfile.run('fun_sieve(200)')
# 3673 function calls in 0.838 seconds