"""
Find the prime below a million, 
that can be expressed as the sum of most consecutive prime.
"""

maximum = 10_000_000 + 1
sieve = [True for _ in range(maximum)]
primes = []

for n in range(2,maximum):
    if sieve[n]:
        primes.append(n)
        for j in range(2*n,maximum,n):
            sieve[j] = False

longest = 0
print(len(primes))



import itertools
def main():
    for offset in itertools.count():
        s = 0
        for p in primes[offset:len(primes)-offset]:
            s+=p
            if s < maximum: continue
            s-=p
            if sieve[s]:
                print(f"{s} is prime too") #997651
                return

main()