dT = lambda n: n+1
dP = lambda n: 3*n+1
dH = lambda n: 4*n+1

n,m,k = 285,165,143
T=P=H=40755

values = {
    "T" : [285,40755,dT],
    "P" : [165,40755,dP],
    "H" : [143,40755,dH],
}

while True:
    min_value = min(values,key=lambda k: values[k][1])
    # print(values["T"][1], values["P"][1], values["H"][1])
    table = values[min_value]
    table[1] += table[2](table[0])
    table[0] += 1

    if values["T"][1] == values["P"][1] == values["H"][1]:
        print(values["T"][1]) # 1533776805
        break


# FUCK, ALL HEXAGON NUMBERS ARE ALSO TRIANGLE NUMBERS
# BRIUHHHHHHHHHHHHH