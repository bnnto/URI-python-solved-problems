C = int(input())
c = 0
while c < C:
    c = c + 1
    i = 0
    n = int(input())
    x = n
    while x > 0:
        if n % x == 0:
            i = i + 1
        x -= 1
    if i == 2:
        print(f"{n} eh primo")
    if i > 2:
        print(f"{n} nao eh primo")
