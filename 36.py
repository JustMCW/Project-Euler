
def is_palindromic(n : str) -> bool:
    n = str(n)

    for i in range(len(n)//2):
        if n[i] != n[-i-1]:
            return False
    
    return True

assert is_palindromic(12321) == True
assert is_palindromic(12331) == False

s = 0
for x in range(1,1_000_000 + 1):
    if is_palindromic(x) and is_palindromic(bin(x)[2:]):
        print(x)
        s += x

print(s)