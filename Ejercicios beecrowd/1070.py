r = []

X = int(input())

for i in range(6):
    if X % 2 == 0:
        X += 1
    r.append(X)
    X += 2  
for val in r:
    print(val)