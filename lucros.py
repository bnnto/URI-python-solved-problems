emprestimo = float(input())
meses = int(input())
taxa = int(input())

if taxa > 1:
    print("A taxa deve ser zero ou um.")
if taxa == 1:
    taxa = 0.01
if taxa == 0:
    taxa = 0
    montante = emprestimo * ((1 + taxa) ** meses)
    juros = montante - emprestimo
    print(f"Ele vai pagar R$ {juros:.2f} de juros!")
