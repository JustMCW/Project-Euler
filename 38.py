"""
192
[1,2,3]

muplity each together

192
384
576

concatenating them, you get 192384576 (concatenated product), it is also 1-9, pandigital as it used 

find largest 1-9 pandigital number formed by concatenated product
where (1,2,...n), n >1
and an unknown interger
"""


"""

THINK INGGG !!!

lets try it from top down, finding all combinations of 123456789 from largest to smallest
see which can be made as a concatenated product
"""

import itertools

x=list("123456789")
a=[i for i in itertools.permutations(x,9)]
all_perm=sorted(a)

def can_be_made_as_con_prod(n : str):
    for i in range(4):
        num = int(n[:i+1])

        temp_str = ""

        # print(num)
        for i in range(1,10):
            temp_str += str((i*int(num)))
            if len(temp_str) == 9:
                if temp_str != n:
                    break
                return True
            elif len(temp_str) > 9:
                break
    return False

for i in range(len(all_perm)-1,1,-1):
    n = "".join(all_perm[i])
    if (can_be_made_as_con_prod(n)):
        print(n)
        break
# print(can_be_made_as_con_prod("192384576"))