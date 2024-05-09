c, q = map(int, input().split(' '))
if c == 1:
    t = 4.00 * q
elif c == 2:
    t = 4.50 * q
elif c == 3:
    t = 5.00 * q
elif c == 4:
    t = 2.00 * q
elif c == 5:
    t = 1.50 * q
print(f"Total: R$ {t:.2f}")

# Outro código possível:

# c, q = map(int, input().split(' '))

# if c == 1:
    # t = 4.00 * q
    # print(f"Total: R$ {t:.2f}")
# if c == 2:
    # t = 4.50 * q
    # print(f"Total: R$ {t:.2f}")
# if c == 3:
    # t = 5.00 * q
    # print(f"Total: R$ {t:.2f}")
# if c == 4:
    # t = 2.00 * q
    # print(f"Total: R$ {t:.2f}")
# if c == 5:
    # t = 1.50 * q
    # print(f"Total: R$ {t:.2f}")
