import timeit

def pow2_1(n):
    power = 2**n
    return power

def pow2_2(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    power = 2
    for i in range(n - 1):
        power *= 2
    return power

def pow2_3(n):
    pass

elapsed_time = timeit.timeit(lambda : pow2_1(10000), number=10000)
print(f"Elapsed time of first pow2 function: {elapsed_time} seconds")

elapsed_time = timeit.timeit(lambda : pow2_2(1000), number=1000)
print(f"Elapsed time of pow2 function using a for loop: {elapsed_time} seconds")