while True:
    V = []
    M, N = map(int, input().split())
    if M <= 0 or N <= 0:
        break
    menor = min(M, N)
    maior = max(M, N)
    for numero in range(menor + 1, maior):
        V.append(numero)
    V.insert(0, menor)
    V.append(maior)
    soma = sum(V)
    print(' '.join(map(str, V)), f"Sum={soma}")