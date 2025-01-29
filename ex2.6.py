import timeit

def pow2_1(n):
    power = 2**n
    return power

elapsed_time = timeit.timeit(lambda : pow2_1(10000), number=10000)
print(f"Elapsed time of first pow2 function: {elapsed_time} seconds")

def pow2_2(n):
    if n == 0:
    
    power = 2
    for i in range(1, n + 1):
        power *= 2
    return power

print(pow2_2(0))