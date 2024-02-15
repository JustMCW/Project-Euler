"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def sum_of_factors(x : int):
    p = 2
    s = 1
    while p*p <= x:
        if x%p == 0:
            s += p
            p2 = int(x/p)
            if p != p2:
                s += p2
        p += 1
    return s
            

def is_amicalbe(n : int) -> bool:
    s = sum_of_factors(n)
    if s == n: return False #Doesn't count if sum of factors is equal to itself
    return n == sum_of_factors(s)

assert is_amicalbe(220) == True

s = 0
for i in range(10,10_001):
   if is_amicalbe(i):
       print(i)
       s += i

print(s)
#31626