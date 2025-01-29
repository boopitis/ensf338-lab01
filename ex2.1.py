import sys
import math

def do_stuff():
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])

    d = b**2 - 4*a*c

    # error fix
    if a == 0:
        print("Invalid input. First value 'a' cannot be zero.")
        exit()

    if d > 0:
        root1 = (-b + math.sqrt(d)) / (2*a)
        root2 = (-b - math.sqrt(d)) / (2*a)
        print(f"The solutions are: {root1}, {root2}")
    elif d == 0:
        root = -b / (2*a)
        print(f"The solution is: {root}")
    else:
        print("There are no real solutions.")

do_stuff()

'''
Solutions:
(i) The code calculates the roots of the quadratic equation based
on the given inputs a, b and c in the command line

(ii) The program does not check for the condition where a == 0, as
this is an invalid quadratic equation, it would also result in
dividing by zero.
'''