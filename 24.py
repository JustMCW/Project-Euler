"""
A permutation is an ordered arrangement of objects. 
For example, 
3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, 
we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

0123456789

0123456798

0123456879
0123456897

0123456978
0123456987

9

89
98

789
879
897

6789
6879

56789


Take
01234
01243

01324
01342

01423
01432

02134
02143

02314
02341

02413
02431

03124
03142

03214
03241

03412
03421
"""

import math

"""
starting at 0th permutation.

the million is actually 999999th cuz 0th is actually the first in PE's indexing

0... +9! permutations (0-362880)...
1... +9! perm  (from 362880 to 725760)
2... +9! (from 725760 to 3 * 9! > 1,000,000 so stop here.)

therefore it's also the lex perm of 0,2,...,8,9 of index 274240

continuing

10... +8! (0 to 40320), skipping 1 because used
12... +8! (40320 to 80640)
 3
 4
 5
16... +8! (5 *8! to 241920) this is it.
17... +8! (241920 to 282240 > 274240)

then find the 274240-241920 = 32320th index of 0,2,3,4,5,6,8,9

LET COMPUTER DO THE TASK

this index can be found through floor division too.
target / k!
"""
final = "" # because 9! < 1_000_000 < 10!

result = ""
target = 1_000_000-1

digits = [0,1,2,3,4,5,6,7,8,9]
length = len(digits)

# Logging version
# for i in range(length-1,-1,-1):
#     print(f"----------iter {i}---------")
#     current_perm_size = math.factorial(i)
#     print(f"{target} - {target // current_perm_size}({current_perm_size}) = ")

#     selected_digit = digits.pop((target // current_perm_size))
#     print(selected_digit, digits)
#     final += str(selected_digit)
#     target -= (target // current_perm_size) * current_perm_size

# final solution
result = ""
target = 1_000_000-1
digits = [0,1,2,3,4,5,6,7,8,9]

for k in range(len(digits)-1,-1,-1):
    current_perm_size = math.factorial(k)
    result += str(digits.pop((target // current_perm_size)))
    target -= (target // current_perm_size) * current_perm_size

print(result)

import itertools
liste="0123456789"
x=list(liste)
a=[i for i in itertools.permutations(x,10)]
b=sorted(a)
# print("".join(b[999999]))
print("".join(b[0]))
print("".join(b[math.factorial(9)-1]))
print("".join(b[2*math.factorial(9)-1]))

# 2783915460