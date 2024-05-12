N = 0
C = int(input())
while N < C:
    X, Y = map(int, input().split())
    if Y != 0:
        div = X / Y
        print(f"{div:.1f}")
    else:
        print("divisao impossivel")
    N += 1