import math

while True:
    try:
        M, N = map(int, input().split())
        result = math.factorial(M) + math.factorial(N)
        print(result)
    except EOFError:
        break