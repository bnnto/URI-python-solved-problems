a, b = map(int, input().split())

if a % b == 0 or b % a == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")

# Outros códigos corretos de múltiplos:

# a, b = map(int, input().split())
# ma = max(a, b)
# mi = min(a, b)
# AB = ma % mi
# if AB == 0:
    # print("Sao Multiplos")
# else:
    # print("Nao sao Multiplos")
# ------------------------------------------
# a, b = map(int, input().split())
# if a > b:
    # m = a
    # AB = m % b
# if b > a:
    # m = b
    # AB = m % a
# if AB == 0:
    # print("Sao Multiplos")
# else:
    # print("Nao sao Multiplos")