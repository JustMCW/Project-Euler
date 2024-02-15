"""S number = perfect sqaure whcih sqaure root can be obtained by spliting the digts and adding up"""

"""
consider 2 digits numbers.

√(10a+b) = a+b
10a+b = a^2 + 2ab + b^2
a^2 - 10a + 2(a)(b) + b^2 - b = 0

a(a-10) + 2ab + b(b-1)
"""
import itertools

def sqaure_gen():
    for i in itertools.count():
        yield i*i

def can_split(perfect_sqaure :int):
    ...

gen = sqaure_gen()
for i in itertools.count():
    n = i*i
    if n > 10**12:
        break
    print(i,n)