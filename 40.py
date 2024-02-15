"""
An irrational decimal fraction is created by concatenating the positive integers:

0.12346789101112131415161718192021...

if can be seen that the 10th digit of fractional part is 1
if can be seen that the 11th digit of fractional part is 0
if can be seen that the 12th digit of fractional part is 1

Find 
d_1 x d_10 x d_100 x d_1,000 x d_10,000 x d_100,000 x d_1,000,000

d_1 = 1
d_10 = 1
"""

"""
THINKING

firstly its determinded on the number of digits it has

1-9 is 9 1-digit number (9)
then followed by 10-99, which contains 90 2-digit numbers (189 digits so far)
100-999, 900 3-digits number (189 + 2700 = 2889)
continuing... we'll find that as we go,
7 digits number will make the number exceed 1m digits, (5888889)


...
Maybe, we can make it converge, by using index

example is if we need to find 1000
3 digits starts at 190 and 4 digits at 2890

there is 900 numbers for 3 digits (100-999)
190 < 1000 < 2890

(1000-190)// 3 + 100 = 370, remainder = 0, digit = 3
adding a hundred because there is also the numbers before.
Use the remained the find the digit of this number

 = floor((10^d - LB) /3) + 10^(d-1)
"""

# Computing the era of each digits. up to 1M.
bounds = [0]

digit = 1
count = 0

p = 6

while count < 10**p:
    count += 9 * digit * (10**(digit-1))
    bounds.append(count+1)
    digit += 1

# numbers means when n-digit era start. 0-9 = 1 digit era, 10-190 = 2digit era
# bounds = [0,10, 190, 2890, 38890, 488890, 5888890]
print(bounds)

def find_digit(index : int):
    digit = 0
    LB = 0

    # finding the LB 
    for i,b in enumerate(bounds):
        if b>index:
            digit = i
            LB = bounds[i-1]
            break

    # finding the number that the index lands on
    # each number contains n-digits, therefore the index of the number is difference / n
    r = (index - LB) // digit

    # every number above 1 digits is offset by the onces before except 1-9
    # 10-99 is missing 1-9, 100-999 is missing 10-99, so just add it.
    if digit > 1:
        r += 10**(digit-1)

    print(r)
    return str(r)[(index - LB)%digit]


product = 1
for i in range(p+1):
    # print(int(find_digit(10**i)))
    product *= int(find_digit(10**i))

print(product) # 210

