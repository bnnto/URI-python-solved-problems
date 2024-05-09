teste = 0
n = int(input())
while n > 0:
    x, v = -10000, -10000
    y, u = 10000, 10000
    for i in range(n):
        entrada = list(map(int, input().split()))
        if entrada[0] > x: x = entrada[0]
        if entrada[1] < y: y = entrada[1]
        if entrada[2] < u: u = entrada[2]
        if entrada[3] > v: v = entrada[3]
    teste += 1
    print(f"Teste {teste}")
    if x < u and v < y:
        print(f"{x} {y} {u} {v}")
    else:
        print("nenhum")
    print()
    n = int(input())