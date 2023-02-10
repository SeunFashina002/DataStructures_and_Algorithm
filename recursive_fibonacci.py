

def fib(n):
    if n>=3:
        return fib(n-1) + fib(n-2)
    else:
        return 1
print(fib(8))
# The number 8 in a fibonacci sequence is --> 21

#---> Formula : FIBn = FIB(n-1) + FIB(n-2)
"""
1, 1, 2, 3, 5, 8, 13, 21

FIB(5) = FIB(4) + FIB(3) : the addition of the 4th and 3rd fibonacci numbers in the sequence --> 5
    FIB(4) = FIB(3) + FIB(2)
        FIB(3) = FIB(2) + FIB(1)
            FIB(3) = 1 + 1 --> 2 --> The number 3 in a fibonacci sequence is 2

FIB(2) = 1 
FIB(1) = 1 

FIB2 = FIB1 + FIB0 : incorrect --> : return 1

"""