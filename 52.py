"""
Find smallest integer x, 
which has the same exact digits but rearranged as 2x, 3x, 4x, 5x, 6x



first digit can only be 1.

second digit (a)
1a
60+6a 6a < 40
a<40/6
a<7

and true for the rest of the digits (max digit value = 6, 6*6 = 36)
"""
import itertools

def has_same_digit(*n):
    
    digits = []

    for num in n:
        if not digits:
            digits = sorted([char for char in str(num)])
            
        elif sorted([char for char in str(num)]) != digits:
            return False

    return True

def satisfy(x :int):
    # print(x)
    return has_same_digit(x, 2*x, 3*x, 4*x, 5*x, 6*x)


i = 1

for p in itertools.count(start=2):
    print(p)
    for n in range(10**p,10**p+int("6"*p)):
        if satisfy(n):
            print(n)
    # break

