"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

"""4^500 = 8^250 = 16^125 = 
32 ^ 62 * 16 = 
64 ^ 31 * 16 = 
128 ^ 15 * 64 * 16
256 ^ 7 * 128 * 64 * 16
512 ^ 3 * 256 * 128 * 64 * 16
"""
print(sum(map(lambda x: int(x),
    list(str(256 ** 125)))
))