

def factorial (x : int):
    if x < 2:
        return 1
    r = 1
    for i in range(2,x+1):
        r *= i
    return r

# assert factorial(3) == 6
# assert factorial(4) == 24
# assert factorial(5) == 120

def sum_of_factorials(n):
    s = 0
    for d in str(n): s += factorial(int(d))
    return s
        

n = 3
sum_ = 0
try:
    while True:
        if sum_of_factorials(n) == n:
            print(n)
            sum_ += n
        n += 1
except KeyboardInterrupt:
    print(sum_)