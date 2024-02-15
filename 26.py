"""
Find longest recurring cycle of 1/d
d<1000.

thoughts :
mutiplying d by 2,5 wont do shit do the recurring

any number that can be expressed as 2^n * 5^m wont be. ( cuz divisible )



OH WAIT SHIT

I checked 1/14 its 0.07142857143, 6 digit recuring... (same as 1/7)
1/7 = 0.142857142
1/21 = 1/7*3 = 0.0476190476 (6)
1/35 = 0.0285714285714 (6)
1/70 = 1/7*10 = 0.0142857142 (6)

1/49 = 1/7*7 = 0.0204081632653061224489795918367346938775510204, (42 digits recuring )



"""
import decimal

def get_rec_length_loop(d):
    cycle = []
    n = 1
    remainder = -1

    while remainder not in cycle:
        n*=10
        cycle.append(remainder)
        remainder = n%d
        # print(n//d, cycle)
        n = remainder
        if remainder == 0: return 0

    return len(cycle)-cycle.index(remainder) # to remove anything thats before but not in the cycle

"""
let R(d) be the number of recuring decimal

R(d) = 0 if d is a divisor of 10^n where n can be any integer. like 2,5,10,25,8 (not even recurring)

Observe:
R(7) = 6
R(49) = 42 = 6*7
R(343) = 294 = 42 * 7

Hypoth : R(a^b) = R(a) * a^(b-1)

Try with 6
R(6) = 1
R(6^2) = 1
R(6^3) = 3
R(6^4) = 9

Hypoth proven false by counter example... However. its still going in 3s
"""

sieve = [True for _ in range(1001)] # we using 1-indexing btw.

# excluding factors of 10, by making 2^n x 5^m all false
p = 0

while 5**p < 1000:
    k = 0
    while (5**p) * (2**k) < 1000:
        nope = (2**k) * (5**p)
        sieve[nope] = False
        k+=1
    p+=1

# for base in range(2,20):
#     if sieve[base]:
#         for power in range(1,5):
#             print(f"R({base}^{power}) = {get_rec_length_loop(base**power)}")
#         print("-"*9)
max_r = 0
n = None
for i in range(1,1001):
    if sieve[i]:
        rec = get_rec_length_loop(i)
        if rec > max_r:
            n = i
            max_r = rec
            print(f"{i} : {rec}")
print(n)




"""
SF = 3
R(3^1) = 1
R(3^2) = 1
R(3^3) = 3
R(3^4) = 9
---------
SF = 3
R(6^1) = 1
R(6^2) = 1
R(6^3) = 3
R(6^4) = 9
---------
SF = 7
R(7^1) = 6
R(7^2) = 42
R(7^3) = 294
R(7^4) = 2058
---------
SF = 9
R(9^1) = 1
R(9^2) = 9
R(9^3) = 81
R(9^4) = 729
---------
SF = 11
R(11^1) = 2
R(11^2) = 22
R(11^3) = 242
R(11^4) = 2662
---------
SF = 3
R(12^1) = 1
R(12^2) = 1
R(12^3) = 3
R(12^4) = 9
---------
SF = 13
R(13^1) = 6
R(13^2) = 78
R(13^3) = 1014
R(13^4) = 13182
---------
SF = 7
R(14^1) = 6
R(14^2) = 42
R(14^3) = 294
R(14^4) = 2058
---------
SF = 3
R(15^1) = 1
R(15^2) = 1
R(15^3) = 3
R(15^4) = 9
---------
SF = 17
R(17^1) = 16
R(17^2) = 272
R(17^3) = 4624


"""