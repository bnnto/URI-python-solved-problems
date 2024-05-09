x, y, z = map(int, input().split())
f = abs(y - x) - z
if f > 0:
    print(f"Folhas sobrando: {f}")
elif f < 0:
    print(f"Folhas faltando: {abs(f)}")
else:
    print("Quantidade de folhas suficientes")

    