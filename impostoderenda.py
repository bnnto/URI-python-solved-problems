salario = float(input())

if salario <= 2000.00:
    print("Isento")
    exit()
if salario <= 3000.00:
    salario = salario - 2000.00
    imposto = 0.08 * salario
    print(f"R$ {imposto:.2f}")
    exit()
if salario <= 4500.00:
    salario = salario - 2000.00
    imposto = (salario - 1000) * 0.18 + 1000 * 0.08
    print(f"R$ {imposto:.2f}")
    exit()
if salario > 4500.00:
    salario = salario - 2000.00
    imposto = (salario - 2500) * 0.28 + 1500 * 0.18 + 1000 * 0.08
    print(f"R$ {imposto:.2f}")
    exit()
