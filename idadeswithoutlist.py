idadesT = 0
c = 0
while True:
    idades = int(input())
    if idades > 0:
        idadesT += idades
        c += 1
    else:
        med = idadesT / c
        print(f"{med:.2f}")
        break