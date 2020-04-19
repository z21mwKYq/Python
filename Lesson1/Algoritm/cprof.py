import cProfile

def get_len(array):
    return  len(array)

def get_sum(array):
    S = 0
    for i in array:
        S +=i
    return S

def main ():
    lst = [i for i in range (1000000)]
    lst = [i for i in range (1000000)]
    a = get_len(lst)
    b = get_sum(lst)

cProfile.run('main()')