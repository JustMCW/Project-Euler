"""
Coded Triangle Numbers

Triangle numbers can be computed using 1/2 x n(n+1)

1,3,6,10,15,21,28,36,45,55...

converting a word such as SKY to a number, 
by using each letters position in the alphabet,
and summing them up :

19+11+25 = 55

55 is a triangle number, and therefore we call SKY a triangle word

How many of the words in 42.txt is a triangle word?
"""

"""
Think :
T = 1/2 x n(n+1)
2T = n^2 + n
0 = n^2 + n - 2T

we check if it has positve interger solution for n.

n = (-1 + √(1+8T)) / 2

only intrested in positive solution btw

1,3,6,10,15,21,28,36,45,55...

if T = 1. n = 1

can √(1+8T) make an even ? T is an integer

ans is no, because the inside has to be even too, 1+8T is odd for any integer T

Therefore we don't even need to consider the whole expression, just consider if √(1+8T) is an int.

"""

from math import sqrt
import itertools
import string

counter = itertools.count()

def word_value(word : str):
    return sum([string.ascii_uppercase.index(char)+1 for char in word.upper()])

def is_triangle_num(T : int):
    return (sqrt(1+8*T)).is_integer()

with open("42.txt","r") as txt:
    words = txt.read().split(",")
    for word in words:
        word = (word.replace("\"",""))
        if is_triangle_num(word_value(word)):
            next(counter)

print(counter) # 162

