i = 0
dias = 0

qnt = int(input())

while i < qnt:
    kg = float(input())
    dias = 0
    while kg > 1:
        kg = kg - (kg * 0.5)
        dias = dias + 1
    print(dias, "dias")
    i += 1