kWh = int(input("Quantidade de kWh consumida: "))
instalacao = input("Digite sua instalação (R, C ou I): ")

preço = 0

if instalacao == "R" and kWh <= 500:
    preço = 0.40
elif instalacao == "R" and kWh > 500:
    preço = 0.65
elif instalacao == "C" and kWh <= 1000:
    preço = 0.55
elif instalacao == "C" and kWh > 1000:
    preço = 0.60
elif instalacao == "I" and kWh <= 5000:
    preço = 0.55
elif instalacao == "I" and kWh > 5000:
    preço = 0.60
else:
    print("ERRO! Tipo de instação errada!")

consumo = kWh * preço
print()
print("Você deve pagar R$ %.2f" % consumo)