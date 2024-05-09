lotes = int(input())
populacao = int(input())

lotes_p = lotes // populacao
lotes_s = lotes % populacao

print(f"Cada pessoa recebera {lotes_p} lotes.")
print(f"Restarão {lotes_s} lotes.")