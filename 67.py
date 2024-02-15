"""
You would want to start from the bottom,
and then pick with 2 adjacent ones, pick the larger one and give it to the top.

why would that give the max?

cuz in the example below, if you were you to get to the number 6, 
9 is always the better option here as there are no more number down.
therefore if you get to 6, the max is 15.

repeat this for every number at the bottom, distrubute it one ro above, repeat til u get to to top.
"""

# Problem 18.
# triagle = [
#      [3,],
#    [7, 4,],
#  [2, 4, 6,],
# [8, 5, 9, 3,]
# ]
# Except 1 year after, im much, much stronger ! Sovle by op method

triagle=[]
with open("67.txt","r") as f:
    for line in f.readlines():
        triagle.append([int(n) for n in line.split(" ")])


triagle.reverse()

for row,row_current in enumerate(triagle):
    if row+1==len(triagle):
        break
    row_above = triagle[row+1]
    # print(row_current,row_above)
    for i,_ in enumerate(row_above):
        row_above[i] += max(row_current[i],row_current[i+1])

print(triagle[-1])