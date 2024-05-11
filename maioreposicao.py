i = 0
NT = []
while i < 100:
    N = int(input())
    NT.append(N)
    i = i + 1
NM = max(NT)
print(NM)
print(NT.index(NM) + 1)