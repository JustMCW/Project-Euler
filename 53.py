"""
Find the number of values from 0<=n<=100

such that nCr > 1,000,000.

nCr = n! / r!(n-r)!



sum of the pascal triangle row is doubled every time

log_2 1,000,000 = 19.93156857... n > 20

r :0 to n inclusive
starting from n=0:
      1 
     1 1
    1 2 1 
   1 3 3 1
  1 4 6 4 1
 1 5 10 10 5 1
1 6 15 20 15 6 1

0,1,2,3,4

wait bruh, if we are using pascals tirangle

a
b b
c c c

c > b > a, meaning any number that is > a million, also has all the number below greater than a 1m

3

"""


# 1,3,6,10,15,21

# n(n+1)/2

# the row index = n - 1
# (or equal if using zero indexing. )

# from 23 to 100
# from 1 to 78
# n = 78
# minimum = 3061

# futhur minimum : 
# there are 4 values in row 23 > 1,000,000
# so we can pretend it starts at 20 with 1 value
# 20 to 100
# 1 to 81 = 3321
# -6 because pretend it starts at 20 but it doesn't

# print(sum(range(4,82)))

import math

target = 1000000
counter = 0

# no need to keep track of values the exceed a million, they just are.
exceed = float("inf")

def next_pascal_row(row):
    temp = []
    temp.append(1)
    for i in range(len(row)):
        if i+2>len(row): break
        if row[i] + row[i+1] > target:
            temp.append(exceed)
        else:
            temp.append(row[i]+row[i+1])

    temp.append(1)
    return temp

c = 0
r = [1]
for i in range(100):
    r = (next_pascal_row(r))
    c += sum([1 if n>=target else 0 for n in r])
    print(i+1,c)

print(c) #4075