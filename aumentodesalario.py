s = float(input())

if 0 <= s <= 400.00:
    p = 15
    r = s * (p / 100)
    ns = s + r
    print(f"Novo salario: {ns:.2f}")
    print(f"Reajuste ganho: {r:.2f}")
    print(f"Em percentual: {p} %")
if 400.01 <= s <= 800.00:
    p = 12
    r = s * (p / 100)
    ns = s + r
    print(f"Novo salario: {ns:.2f}")
    print(f"Reajuste ganho: {r:.2f}")
    print(f"Em percentual: {p} %")
if 800.01 <= s <= 1200.00:
    p = 10
    r = s * (p / 100)
    ns = s + r
    print(f"Novo salario: {ns:.2f}")
    print(f"Reajuste ganho: {r:.2f}")
    print(f"Em percentual: {p} %")
if 1200.01 <= s <= 2000.00:
    p = 7
    r = s * (p / 100)
    ns = s + r
    print(f"Novo salario: {ns:.2f}")
    print(f"Reajuste ganho: {r:.2f}")
    print(f"Em percentual: {p} %")
if s > 2000.00:
    p = 4
    r = s * (p / 100)
    ns = s + r
    print(f"Novo salario: {ns:.2f}")
    print(f"Reajuste ganho: {r:.2f}")
    print(f"Em percentual: {p} %")
