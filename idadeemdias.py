idade = int(input())

ano = idade // 365
iA = (idade % 365)
meses = iA // 30
dias = iA % 30

print(ano, "ano(s)")
print(meses, "mes(es)")
print(dias, "dia(s)")
