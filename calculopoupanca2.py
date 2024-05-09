dp = float(input("Qual é o depósito inicial: "))
taxa = int(input("Qual é a taxa de juros: "))
dpm = float(input("Depósito mensal: "))
t = taxa / 100
i = 0
i2 = 1
M = dp
while i <= 24 and i2 <= 24:
    M = M + (M * t) + dpm
    J = M - dp
    print("Valor do mês %d: R$ %5.2f" % (i2, M))
    i2 = i2 + 1
    i = i + 1
print(f'Total ganho com juros: R$ {J:.2f}')