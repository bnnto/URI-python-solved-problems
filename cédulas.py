cedulas = int(input())
print(cedulas)
cem = 0
cinq = 0
vinte = 0
dez = 0
cinco = 0
dois = 0
um = 0

if cedulas >= 100:
    cem = cedulas // 100
    cedulas = cedulas - (cem * 100)
if cedulas >= 50:
    cinq = cedulas // 50
    cedulas = cedulas - (cinq * 50)
if cedulas >= 20:
    vinte = cedulas // 20
    cedulas = cedulas - (vinte * 20)
if cedulas >= 10:
    dez = cedulas // 10
    cedulas = cedulas - (dez * 10)
if cedulas >= 5:
    cinco = cedulas // 5
    cedulas = cedulas - (cinco * 5)
if cedulas >= 2:
    dois = cedulas // 2
    cedulas = cedulas - (dois * 2)
if cedulas >= 1:
    um = cedulas // 1
    cedulas = cedulas - (um * 1)

print(cem, "nota(s) de R$ 100,00")
print(cinq, "nota(s) de R$ 50,00")
print(vinte, "nota(s) de R$ 20,00")
print(dez, "nota(s) de R$ 10,00")
print(cinco, "nota(s) de R$ 5,00")
print(dois, "nota(s) de R$ 2,00")
print(um, "nota(s) de R$ 1,00")


