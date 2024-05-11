# Utilize os tipos em maiusculo [C, R , S]
i = 0
N = int(input())
listaN = []
CO = 0
RA = 0
SA = 0
while i < N:
    Q, T = input().split()
    Q = int(Q)
    listaN.append(Q)
    if T == 'C':
        CO = CO + Q
    if T == 'R':
        RA = RA + Q
    if T == 'S':
        SA = SA + Q
    i = i + 1
print(f"Total: {sum(listaN)} cobaias")
print(f"Total de coelhos: {CO}")
print(f"Total de ratos: {RA}")
print(f"Total de sapos: {SA}")
print(f"Percentual de coelhos: {(CO / sum(listaN)) * 100:.2f} %")
print(f"Percentual de ratos: {(RA / sum(listaN)) * 100:.2f} %")
print(f"Percentual de sapos: {(SA / sum(listaN)) * 100:.2f} %")