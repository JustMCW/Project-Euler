"""
Sub-string Divisibility

A number, 1406357289 is 0-9 pandigital. (used all digits from 0-9)

but also it has some intresting substring property

let dn but the digit indexed at n

d2d3d4 = 406 is divisible by 2
d3d4d5 = 063 is divisible by 3
d4d5d6 = 635 is divisible by 5
d5d6d7 = 357 is divisible by 7
d6d7d8 = 572 is divisible by 11
d7d8d9 = 728 is divisible by 13
d8d9d10 = 289 is divisible by 17

Find sum of all 0-9 pand numbers that share this property 

( the question did not state exactly what property )
"""

"""
THINKING:

R1. d2d3d4 % 2 = 0 <-> d4 can only be 0,2,4,6,8.
R2. d3d4d5 % 3 = 0 <-> d3+d4+d5 % 3 = 0

from R1 since d4 is even, d3 + d5 must be odd -> only one of d3,d5 is odd

R3. d4d5d6 % 5 = 0 <-> d6 can only be 0 or 5.

from R3, d6

no rule for d1 yet



"""

import itertools
import string

odds = range(1,11,2)
evens = range(0,10,2)

def has_property(n : int):
    _,_,d3,d4,d5,d6,d7,d8,d9,d10 = map(int,str(n))
    

    if d4 not in evens: return False
    if d6 not in [0,5]: return False
    div_3 = (d3 + d4 + d5) % 3 == 0
    div_7 = (100*d5 + 10*d6 + d7) % 7 == 0
    div_11 = (100*d6 + 10*d7 + d8) % 11 == 0
    div_13 = (100*d7 + 10*d8 + d9) % 13 == 0
    div_17 = (100*d8 + 10*d9 + d10) % 17 == 0

    return div_3 and div_7 and div_11 and div_13 and div_17
    
s = 0

for p in itertools.permutations(string.digits,len(string.digits)):
    if p[0] =="0": continue
    p = int("".join(p))
    if has_property(p):
        s+=p

print(s) # 16695334890

# [1,2,3,4,5] # insert
# [1,2,0,3,4,5] # insert at 2