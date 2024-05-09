C = int(input())
c = 0
while c < C:
    c = c + 1
    i = 0
    n = int(input())
    x = n - 1
    while x > 0:
        if n % x == 0:
            i = i + x
        x -= 1
    if i == n:
        print(f"{n} eh perfeito")
    if i != n:
        print(f"{n} nao eh perfeito")
