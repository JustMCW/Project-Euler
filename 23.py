"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

def is_abundant(x : int):
    p = 2
    s = 1
    while p*p <= x:
        if x%p == 0:
            s += p
            p2 = int(x/p)
            if p != p2:
                s += p2
        p += 1
    return x < s

abundant_numbers = []
can_be_expressed = set()
sums = 0
limit = 28123

for i in range(1,limit+1):
    sums += i
    if is_abundant(i):
        abundant_numbers.append(i)
        for n in abundant_numbers:
            add_up = i+n
            if add_up <= limit:
                can_be_expressed.add(add_up)

print(sums-sum(can_be_expressed)) #4,179,871