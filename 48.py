"""
find last ten digtis of 1^1 + 2^2 ... 1000^1000.
"""

s= 0
for i in range(11):
    s += pow(i,i)

print(len(str(s)))
print(str(s)[-10:])