i, f = map(int, input().split())

if i > f:
    a = 24 - i
    h = a + f
    print("O JOGO DUROU", h, "HORA(S)")
if f > i:
    h = f - i
    print("O JOGO DUROU", h, "HORA(S)")
if i == f:
    h = 24
    print("O JOGO DUROU", h, "HORA(S)")
