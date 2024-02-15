"""
Find index of the first number in fib seq that contains 1000 digits

1. 1
2. 1
3. 2
4. 3
...
?. >= 10^999
"""

# Noob brute force solution :
F_1 = 1
F_2 = 1

i = 1
while F_1 <= 10**999: 
    # print(f"{i}, {len(str(F_1))}")
    i+=1
    F_1, F_2 = F_2, F_1+F_2

print(i)






"""
APPARENTLY
YOU CAN SOLVE WITH GOLDEN RATIO
phi = (1+√5) / 2

apparently as n gets big

F_2 / F_1 approach golden ratio, phi

phi^n would give an approximation 


phi^n > 10^999
n ln(phi) > 999ln(10)
n > 999ln(10) / ln(phi)

and find the first n integer that satisft this

1. 1
2. 1
3. 2
4. 3
5. 5
6. 8
7. 13
8. 21
9. 34
10. 55
11. 89
12. 144

144 * phi^(n-12) > 10^999
ln(144) + (n-12)ln(phi) > 999ln10
ln(144) + nln(phi) - ln(phi) > 999ln10
ln(144) + n ln((1+√5) / 2) - ln((1+√5) / 2) > 999ln10
2ln(12) + n(ln(1+√5) - ln2) - ln(1+√5) + ln2 > 999ln10
n(ln(1+√5) - ln2) > 999ln10 - ln2 +ln(1+√5) - 2ln(12)
n > (999ln10 - ln2 +ln(1+√5) - 2ln(12)) / (ln(1+√5) - ln2)

n > (999ln2 + 999ln5 - ln2 + ln(1+√5) - 4ln(2) - 2ln(3)) / (ln(1+√5) - ln2)
n > (994ln2 + 999ln5 + ln(1+√5) - 2ln(3)) / (ln(1+√5) - ln2)

if base=2... (log here = log_2)
n > (994 + 999log5 + log(1+√5) - 2log(3)) / (log(1+√5) - 1)

and n is an integer
"""


#Golden ratio'd : pro soultion
from  math import sqrt,log2,ceil

log2_one_plus_root5 = log2(1 + sqrt(5))

# n =(999*log2(10) - 1 + log2_one_plus_root5) / (log2_one_plus_root5 - 1)
n = (994 + 999*log2(5)+log2_one_plus_root5-2*log2(3)) / (log2_one_plus_root5 - 1)
closest_interger = ceil(n)
print(closest_interger)