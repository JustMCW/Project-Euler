def is_prime(n) -> bool:
    if n < 2 or n%2 == 0:
        return False
    p = 3
    while p*p < n:
        if n%p == 0:
            return False
        p += 2
    return True

max_n = 1
max_product = 0
import time
t = time.perf_counter()
for scaler in range(-999,1000):
    for coeffcient in range(-1000,1001):
        n = 0    
        while n < coeffcient:
            r = n * (scaler + n) + coeffcient

            if is_prime(r):
                n += 1
            else:
                break

        if n >= max_n:
            max_n = n
            max_product = coeffcient * scaler
print(max_product)
assert max_product == -59231
print(time.perf_counter()-t)
