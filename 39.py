"""
If p is the perimeter of a right angle triangle with integer length sides,{a,b,c} , 
there are exactly three solutions for.

, , 

For which value of p <= 1000, is the number of solutions maximised?
"""

"""
c is the longest side
c > a,b
but a+b > c
a^2 = c^2 - b^2
"""

# for p in range(1,1001):
#     for a in range(p):
#         print(a)
import math

p_dict = [0 for _ in range(1002)]
print(len(p_dict))
for a in range(1,1001):
    for b in range(1,1001):
        c = math.sqrt(a*a + b*b)
        if c==math.floor(c) and a+b+c <= 1000:
            p_dict[int(a+b+c)] += 1
print(p_dict.index(max(p_dict)))