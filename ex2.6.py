import timeit

# calculates n-th power of 2
def pow2_1(n):
    power = 2**n
    return power

# for loop version
def pow2_2(n):
    pwrs_of_two = []
    for i in range(1, n + 1):
        pwrs_of_two.append(pow2_1(i))
    return pwrs_of_two

# list comprehension version
def pow2_3(n):
    pwrs_of_two = [pow2_1(i) for i in range(1, n + 1)]
    return pwrs_of_two

# total time to calculate pow2_1(10000) 10000 times
elapsed_time = timeit.timeit(lambda : pow2_1(10000), number=10000)
print(f"Elapsed time of pow2_1 function: {elapsed_time} seconds")

# total time to calculate and store powers of 2 up to the 1000th power in an array
# 1000 times using a for loop
elapsed_time = timeit.timeit(lambda : pow2_2(1000), number=1000)
print(f"Elapsed time of pow2_2 function (for loop): {elapsed_time} seconds")

# total time to calculate and store powers of 2 up to the 1000th power in an array
# 1000 times using list comprehension
elapsed_time = timeit.timeit(lambda : pow2_3(1000), number=1000)
print(f"Elapsed time of pow2_3 function (list comprehension): {elapsed_time} seconds")
