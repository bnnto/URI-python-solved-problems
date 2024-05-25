N = int(input())
fat = 1
for i in range(N, 0, -1):
    fat *= i
print(fat)