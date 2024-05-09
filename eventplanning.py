import sys
while True:
    line = sys.stdin.readline()
    if line == '':
        break
    N, B, H, W = map(int, line.split())
    costMin = B + 1
    h = 0
    while h < H:
        price = int(input())
        cost = N * price
        weeks = map(int, input().split())
        w = 0
        while w < W:
            beds = next(weeks)
            if cost < costMin and beds >= N:
                costMin = cost
            w += 1
        h += 1
    if costMin <= B:
        print(costMin)
    else:
        print("stay home")