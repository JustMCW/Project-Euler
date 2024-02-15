"""
We shall say that an n-digit number is pandigital 
if it makes use of all the digits 1 to n exactly once. 
For example, 2143 is a 4-digit pandigital and is also prime.

Find largest n-pand number that is also prime.
"""

"""Maybe, sieve?

nah lets just check all pad numbers from largest to smallest


prime can't end in 2,4,6,8,5

Ho? (Forum solution)
Note: Nine numbers cannot be done (1+2+3+4+5+6+7+8+9=45 => always dividable by 3)
Note: Eight numbers cannot be done (1+2+3+4+5+6+7+8=36 => always dividable by 3)
"""


def is_prime(n) -> bool:
    # print(n)
    # if n == 2143:
    #     print("hi")
    if n < 2 or n%2 == 0:
        return False
    p = 3
    while p*p < n:
        if n%p == 0:
            return False
        p += 2
    return True

import itertools

for n in range(7,0,-1):
    x= [str(i+1) for i in range(n)]
    a = [i for i in itertools.permutations(x,n)]
    all_perm= sorted(a,reverse=True)

    for i in range(0,len(all_perm)):
        if is_prime(int("".join(all_perm[i]))):
            print("".join(all_perm[i])) #7652413, 4231
            break