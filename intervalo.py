v = float(input())

if 0.00 <= v <= 25.00:
    print("Intervalo [0,25]")
if 25.00 < v <= 50.00:
    print("Intervalo (25,50]")
if 50.00 < v <= 75.00:
    print("Intervalo (50,75]")
if 75.00 < v <= 100.00:
    print("Intervalo (75,100]")
if v < 0.00 or v > 100.00:
    print("Fora de intervalo")