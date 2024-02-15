"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
import time

def ez(n : int) -> int:
    from math import factorial
    t = time.perf_counter()
    r = sum(map(lambda x: int(x), list(str(factorial(n)))))
    print(time.perf_counter()-t)
    return r

def prime_factors_of(n : int,factors : list):
    p = 2
    while p*p <= n:
        if n%p == 0:
            factors.append(p)
            return prime_factors_of(int(n/p),factors)
        p += 1
    factors.append(n)
    return factors


def find_sum_of_digits_for_factorial(n : int)-> int:
    t = time.perf_counter()
    l = {}
    print("Factorising ...")
    for i in range(2,n+1):
        fctrs = prime_factors_of(i,[])
        for f in fctrs:
            try:
                l[f] += 1
            except KeyError:
                l[f] = 1
    print("Simplfying ...")
    r = 1
    for k,v in l.items():
        if 10%k == 0:
            k2 = int(10/k)
            remove = min(v,l[k2])
            
            l[k] -= remove
            l[k2] -= remove

    print("Calculating ...")
    for k,v in l.items():
        r *= k**v
    print(time.perf_counter() - t)
    #Calculating the sums of the digits
    return sum(map(lambda x: int(x), list(str(r))))

size = 1000000
print(find_sum_of_digits_for_factorial(size))
print(ez(size))
# assert ez(100) == 648
# assert find_sum_of_digits_for_factorial(100) == 648
#648