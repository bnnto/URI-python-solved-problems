I = 0
while I <= 20:
    c = 0
    J = 10
    while c < 3 and J <= 30:
        if I % 10 == 0 and (J + I) % 10 == 0:
            print(f"I={int(I/10)} J={int((J + I)/10)}")
        else:
            print(f"I={I/10:.1f} J={round((J + I)/10, 1)}")
        J += 10
        c += 1
    I += 2