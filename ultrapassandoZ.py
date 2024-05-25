X = int(input())
Z = 0
v = []
soma = 0
while Z <= X:
    Z = int(input())
    while soma <= Z:
        v.append(X)
        soma += X
        X += 1
print(len(v))