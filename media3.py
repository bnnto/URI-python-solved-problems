n1, n2, n3, n4 = map(float, input().split(' '))
media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10
if media < 5.0:
    print(f"Media: {media:.1f}")
    print("Aluno reprovado.")
if 5.0 <= media <= 6.9:
    print(f"Media: {media:.1f}")
    print("Aluno em exame.")
    exam = float(input())
    print(f"Nota do exame: {exam:.1f}")
    media_final = (media + exam) / 2
    print("Aluno aprovado.")
    print(f"Media final: {media_final:.1f}")
if media >= 7.0:
    print(f"Media: {media:.1f}")
    print("Aluno aprovado.")