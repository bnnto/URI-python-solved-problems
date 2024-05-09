a, b, c = map(float, input().split(' '))

perimetro = a + b + c
area = ((a + b) * c) / 2
x = 0

if abs(b - c) < a < b + c:
    x = x + 1
if abs(a - c) < b < a + c:
    x = x + 1
if abs(a - b) < c < a + b:
    x = x + 1
if x == 3:
    print(f"Perimetro = {perimetro:.1f}")
else:
    print(f"Area = {area:.1f}")
