T = int(input())
fs = []
i = 0
while i < T:
    N = int(input())
    fs.append(0)
    fs.append(1)
    for x in range(2, 61):
        prox_n = fs[-1] + fs[-2]
        fs.append(prox_n)
    print(f"Fib({N}) = {fs[N]}")
    i += 1