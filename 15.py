# [1,2,3,4]

# 1,2,3
# 2,3,4
# 1,3,4
# 1,2,4
# Order doesn't matter

# length C pick

# 4 ways of picking 1 person
# 6 ways of pick 2 person
# 4 ways of picking 3 person
# n! / r!(n-r)! 

#Pick 20 from 40 
from math import factorial
print(factorial(40)/ (factorial(20) * factorial(40-20)))

# 5 x 4 