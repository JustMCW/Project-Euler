length = 1_000_000
primes = [True for _ in range(length+1)]

p = 2

while p * p < length:
    if primes[p] == True:
        for i in range(p*p,length+1,p):
            primes[i] = False
    p += 1
from collections import deque
def all_rotations(x) -> list[int]:
    x = str(x)
    dq = deque(x)
    r = []
    for _ in range(len(x)):
        r.append(int(''.join(dq)))
        dq.rotate()
    return r
c = 0

for n in range(2,length):
    if primes[n]:
        rotations = all_rotations(n)
        if all(map(lambda x: primes[x] == True, rotations)):
            print(n)
            c += 1
print(c)
#55