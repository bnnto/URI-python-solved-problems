import math
A, B, C = map(float, input().split(' '))

delta = (B ** 2.0) - (4.0 * A * C)

if A > 0 and delta > 0:
    tA = 2.0 * A
    R1 = ((-B) + math.sqrt(delta)) / tA
    R2 = ((-B) - math.sqrt(delta)) / tA
    print(f"R1 = {R1:.5f}")
    print(f"R2 = {R2:.5f}")
else:
    print("Impossivel calcular")