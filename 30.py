sum_n = 0

def f(x : int):
    x = str(x)
    sum_x = 0
    for d in x:
        sum_x += int(d) ** 5
    return sum_x


try:
    for n in range(2,100000000000):
            if f(n) == n:
                print(n)
                sum_n += n
except KeyboardInterrupt:
    print(sum_n)


