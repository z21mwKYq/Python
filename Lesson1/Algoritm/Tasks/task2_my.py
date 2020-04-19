import cProfile
def nbr(num):
    ll = 0
    i = 1
    while True:
        for k in range(2,i+1):
            # print(f' i {i}')
            if i == 2:
                ll += 1
            elif i % k == 0:
                break
            elif i % k != 0 and k == (i-1):
                ll += 1
        if ll == num:
            # print(i)
            # exit (1)
            return i
        i += 1
cProfile.run('nbr(200)')
# timeit

# "import task2_my" "task2_my.nbr(10)"
# 1000 loops, best of 5: 93 usec per loop

#  "import task2_my" "task2_my.nbr(100)"
# 1000 loops, best of 5: 13 msec per loop

# "import task2_my" "task2_my.nbr(200)"
# 1000 loops, best of 5: 57 msec per loop

# cProfile
# cProfile.run('nbr(10)')
# 4 function calls in 0.000 seconds

# cProfile.run('nbr(100)')
# 4 function calls in 0.014 seconds

# cProfile.run('nbr(200)')
# 4 function calls in 0.059 seconds
