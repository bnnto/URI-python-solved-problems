v = []
while True:
    idades = int(input())
    v.append(idades)
    v2 = [idades for idades in v if idades >= 0]
    if idades < 0:
        med = sum(v2) / len(v2)
        print(f"{med:.2f}")
        break