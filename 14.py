def get_step(n):
    counter = 0
    while n != 1:
        if n % 2 == 1:
            n = 3*n + 1
        else:
            n /= 2
        counter += 1
    return counter

larg = 0
final = 0

for i in range(1,1_000_000):
    col = get_step(i)

    if col > larg:
        larg = col
        final = i
        print(i)

print(final,larg)