seqeunce = {}

for a in range(2,101):
    for b in range(2,101):
        seqeunce[a**b] = None

print(len(seqeunce.keys()))