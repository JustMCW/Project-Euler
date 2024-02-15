length = 1_000_000

primes = [True for _ in range(length)]
primes[1] = False # Fuck you
#Sieve
p = 2
while p * p < length:
    if primes[p] == True:
        for i in range(p*p,length,p):
            primes[i] = False
    p += 1

def all_truncates(x) -> list[int]:
    x = str(x)
    l = list(x)
    r = []
    for _ in range(len(x)):
        r.append(int(''.join(l)))
        l.pop(0) 
    l = list(x)
    for _ in range(len(x)):
        r.append(int(''.join(l)))
        l.pop()
    return r

sum_ = 0
c = 0

for n in range(3,length,2):
    if primes[n] and n > 10:
        ts= all_truncates(n)
        if all(map(lambda x: primes[x], ts)):
            sum_ += n
print(sum_)