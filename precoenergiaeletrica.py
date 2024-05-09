kwh = int(input("Quantidade de kWh consumida: "))
tdI = input("Tipo de instalação (R, C ou I): ")
if tdI == "R":
    if kwh <= 500:
        precoF = kwh * 0.40
    else:
        precoF = kwh * 0.65
elif tdI == "C":
    if kwh <= 1000:
        precoF = kwh * 0.55
    else:
        precoF = kwh * 0.60
elif tdI == "I":
    if kwh <= 5000:
        precoF = kwh * 0.55
    else:
        precoF = kwh * 0.60
else:
    precoF = 0
    print("Erro ! Tipo de instalação desconhecido!")
print(f"O preço a ser pago é de R$ {precoF:.2f}.")