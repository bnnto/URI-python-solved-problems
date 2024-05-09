dinheiro = float(input())
cem = 0
cinq = 0
vinte = 0
dez = 0
cinco = 0
dois = 0
um = 0
cinq_cent = 0
vincin_cent = 0
dez_cent = 0
cinco_cent = 0
um_cent = 0

if dinheiro >= 100:
    cem = dinheiro // 100
    dinheiro = dinheiro - (cem * 100)
if dinheiro >= 50:
    cinq = dinheiro // 50
    dinheiro = dinheiro - (cinq * 50)
if dinheiro >= 20:
    vinte = dinheiro // 20
    dinheiro = dinheiro - (vinte * 20)
if dinheiro >= 10:
    dez = dinheiro // 10
    dinheiro = dinheiro - (dez * 10)
if dinheiro >= 5:
    cinco = dinheiro // 5
    dinheiro = dinheiro - (cinco * 5)
if dinheiro >= 2:
    dois = dinheiro // 2
    dinheiro = dinheiro - (dois * 2)
if dinheiro >= 1:
    um = dinheiro // 1
    dinheiro = dinheiro - (um * 1)
if dinheiro >= 0.50:
    cinq_cent = dinheiro // 0.50
    dinheiro = dinheiro - (cinq_cent * 0.50)
if dinheiro >= 0.25:
    vincin_cent = dinheiro // 0.25
    dinheiro = dinheiro - (vincin_cent * 0.25)
if dinheiro >= 0.10:
    dez_cent = dinheiro // 0.10
    dinheiro = dinheiro - (dez_cent * 0.10)
if dinheiro >= 0.05:
    cinco_cent = dinheiro // 0.05
    dinheiro = dinheiro - (cinco_cent * 0.05)
if dinheiro >= 0.01:
   um_cent = dinheiro // 0.01
   dinheiro = dinheiro - (um_cent * 0.01)
if round(dinheiro,2) == 0.01:
    um_cent = 1.00

print("NOTAS:")
print(f"{cem:.0f} nota(s) de R$ 100.00")
print(f"{cinq:.0f} nota(s) de R$ 50.00")
print(f"{vinte:.0f} nota(s) de R$ 20.00")
print(f"{dez:.0f} nota(s) de R$ 10.00")
print(f"{cinco:.0f} nota(s) de R$ 5.00")
print(f"{dois:.0f} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{um:.0f} moeda(s) de R$ 1.00")
print(f"{cinq_cent:.0f} moeda(s) de R$ 0.50")
print(f"{vincin_cent:.0f} moeda(s) de R$ 0.25")
print(f"{dez_cent:.0f} moeda(s) de R$ 0.10")
print(f"{cinco_cent:.0f} moeda(s) de R$ 0.05")
print(f"{um_cent:.0f} moeda(s) de R$ 0.01")