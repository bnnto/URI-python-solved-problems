x = float(input("Digite um número: "))
y = float(input("Digite outro número: "))
operacao = input("Digite um operador (+, -, * e /): ")

if operacao == "+":
    soma = x + y
    print("SOMA =", soma)
elif operacao == "-":
    subtracao = x - y
    print("SUBTRAÇÃO =", subtracao)
elif operacao == "*":
    multiplicacao = x * y
    print("MULTIPLICAÇÃO =", multiplicacao)
elif operacao == "/":
    divisao = x // y
    print("DIVISÃO =", divisao)
else:
    print("Operação inválida!")


