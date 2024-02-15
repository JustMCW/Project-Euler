def simplfy(n,d) -> tuple[int]:
    for p in range(2,n+1):
        if n%p == 0 and d%p == 0:
            return simplfy(int(n/p),int(d/p))
    return n,d

def remove_once(string:str,rm:str) -> str:
    r_str = ""
    for char in string:
        if char == rm:
            rm = None
        else:
            r_str += char
    return r_str

def is_valid_curios(x : int,y : int) -> bool:

    sx = str(x)
    sy = str(y)

    similar_d = None
    for d in sx:
        if d in sy:
            similar_d = d

    if not similar_d: #No similar digit
        return False
    elif similar_d == "0": #no trivial
        return False

    try:
        r = int(remove_once(sx,similar_d)) / int(remove_once(sy,similar_d))
    except (ZeroDivisionError,ValueError):
        return False
    return x/y == r

product_numer = 1
product_denom = 1

for numer in range(10,100):
    for denom in range(10,100):
        if numer < denom: # Less than one
            if is_valid_curios(numer,denom):
                product_numer *= numer
                product_denom *= denom


print(simplfy(product_numer,product_denom))