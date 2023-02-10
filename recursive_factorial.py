# formula = n * (n - 1)

def fact(n):
    if n >= 1:
        return n * fact(n-1)
    else:
        return 1

print(fact(4))        

"""

n * (n-1)
n = 3

3 * fact(3-1) --> 2 * fact(2-1) --> 1 * fact(1-1) --> 1 * fact(0) --> 1 * 1 = 1
4 * fact(4-1) --> 3 * fact(3-1) --> 2 * fact(2-1) --> 1 * fact(1-1) --> 1 * fact(0) --> 1 * 1 = 1

"""