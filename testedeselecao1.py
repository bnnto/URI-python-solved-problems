A, B, C, D = map(int, input().split(' '))

CD = C + D
AB = A + B
tA = A % 2
if B > C and D > A and CD > AB and C > 0 and D > 0 and tA == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")