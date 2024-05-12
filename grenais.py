tgI = []
tgG = []
x = 0
y = 0
z = 0
while True:
    gI, gG = map(int, input().split())
    tgI.append(gI)
    tgG.append(gG)
    teste = int(input("Novo grenal (1-sim 2-nao)\n"))
    if gI > gG:
        x = x + 1
    if gG > gI:
        y = y + 1
    if gI == gG:
        z = z + 1
    if x > y:
        T = 'Inter'
    if y > x:
        T = 'Gremio'
    if teste == 2:
        print(f"{len(tgG)} grenais")
        print(f"Inter:{x}")
        print(f"Gremio:{y}")
        print(f"Empates:{z}")
        if x == y:
            print("Nao houve vencedores")
        else:
            print(f"{str(T)} venceu mais")
        break