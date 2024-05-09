a, b, c, d = map(int, input().split())
b = a * 60 + b
d = c * 60 + d
t = d - b
if t <= 0:
    t = 24 * 60 + t
h = t // 60
m = t % 60
print(f"O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)")
