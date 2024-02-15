"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

words_ones = ["","one","two","three","four","five","six","seven","eight","nine","ten"]
words_teens = ["","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
words_tens = ["","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
def to_word(n : int) -> str:
    string = str(n)
    first_d = int(string[0])
    if n <= 10:
        return words_ones[n]
    elif n < 20:
        return words_teens[n-10]
    elif n <= 99:
        return words_tens[first_d] + words_ones[int(string[1])]
    elif n < 1000:
        hundred = words_ones[first_d] + "Hundred"
        left = n - first_d * 100
        if left == 0:
            return hundred
        elif left < 20:
            return hundred + "And" + to_word(left)
        else:
            return hundred + "And" + words_tens[int(string[1])] + words_ones[int(string[2])]
    elif n == 1000:
        return "OneThousand"

assert len(to_word(342)) == 23
assert len(to_word(115)) == 20

s = 0
d = {}
for n in range(1,1001):
    a = to_word(n)
    d[n] = a
    s += len(a)

# import json
# with open("17.json","w") as f:
#     json.dump(d,f,indent=4)

assert s==21124
print(s)

#this question is rather a english question