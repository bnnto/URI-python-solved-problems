a, b, c, n = map(int, input().split(' '))
x = 0

if 0 < a <= 10 and 0 < b <= 10 and 0 < c <= 10 and 1 <= n <= 20:
    print("YES")
else:
    print("NO")

    # second option:
# if 0 < a <= 10:
    # x = x + 1
# if 0 < b <= 10:
    # x = x + 1
# if 0 < c <= 10:
    # x = x + 1
# if 1 <= n <= 20:
    # x = x + 1
# if x == 4:
    # print("YES")
# else:
    # print("NO")
