a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())

testeA = a % 2
testeB = b % 2
testeC = c % 2
testeD = d % 2
testeE = e % 2
x = 0

if testeA == 0:
    x = x + 1
if testeB == 0:
    x = x + 1
if testeC == 0:
    x = x + 1
if testeD == 0:
    x = x + 1
if testeE == 0:
    x = x + 1
if x == 1 or x == 2 or x == 3 or x == 4 or x == 5:
    print(x, "valores pares")
