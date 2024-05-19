N = int(input())
fs = []

if N > 0:
    fs.append(0)
if N > 1:
    fs.append(1)

for i in range(2, N):
    prox_n = fs[-1] + fs[-2]
    fs.append(prox_n)
print(" ".join(map(str, fs)))