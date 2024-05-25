# Digite 1. Álcool 2. Gasolina 3. Diesel 4. Fim
al = 0
ga = 0
di = 0
while True:
    T = int(input())
    if T == 1:
        al += 1
    elif T == 2:
        ga += 1
    elif T == 3:
        di += 1
    elif T == 4:
        print("MUITO OBRIGADO")
        print(f"Alcool: {al}")
        print(f"Gasolina: {ga}")
        print(f"Diesel: {di}")
        break