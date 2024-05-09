A, B, C = map(float, input().split())
lM = max(A, B, C)
lMEN = min(A, B, C)
lMEI = (A + B + C) - (lM + lMEN)
B2C2 = lMEI ** 2 + lMEN ** 2
A2 = lM ** 2
if lM >= (lMEI + lMEN):
    print("NAO FORMA TRIANGULO")
    exit()
if A2 == B2C2:
    print("TRIANGULO RETANGULO")
if A2 > B2C2:
    print("TRIANGULO OBTUSANGULO")
if A2 < B2C2:
    print("TRIANGULO ACUTANGULO")
if A == B == C:
    print("TRIANGULO EQUILATERO")
    exit()
if A == B or A == C or B == C:
    print("TRIANGULO ISOSCELES")
