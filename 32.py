"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

"""
sums = {}

def is_9_pandigital(x : int, y : int, z : int) -> bool:
    joined = str(x)+str(y)+str(z)
    if "0" in joined: return False
    for i in range(1,10):
        if joined.count(str(i)) != 1:
            return False
    return True

for multipld in range(1,10000):
    for multiplr in range(1,10000):
        r = multipld * multiplr
        if r < 10000:
            if is_9_pandigital(multipld,multiplr,r):
                sums[r] = None

print(sum(sums.keys()))
#45228


