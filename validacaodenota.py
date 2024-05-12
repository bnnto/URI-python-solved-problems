tNo = []
while True:
    nota = float(input())
    if 0.0 <= nota <= 10.0:
        tNo.append(nota)
        if len(tNo) == 2:
            print(f"media = {sum(tNo) / 2}")
            break
    else:
        print("nota invalida")