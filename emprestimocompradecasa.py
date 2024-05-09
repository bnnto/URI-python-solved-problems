v = float(input("Qual é o valor da casa: "))
s = float(input("Qual é o valor do seu salário: "))
qa = float(input("Qual a quantidade de anos a pagar: "))
qm = 12 * qa
p = v / qm
if p > s * 0.3:
    print("Infelizmente você não pode obter o empréstimo.")
else:
    print(f"Valor da prestação: R$ {p:.2f} Empréstimo OK")