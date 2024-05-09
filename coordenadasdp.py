x, y = map(float, input().split(' '))

if x == 0 and y == 0:
    print("Origem")
elif x > 0 and y > 0:
    print("Q1")
elif y > 0 > x:
    print("Q2")
elif x < 0 and y < 0:
    print("Q3")
elif x > 0 > y:
    print("Q4")
elif x == 0:
    print("Eixo Y")
else:
    print("Eixo X")

# Duas outras formas de fazer o código:

# x, y = map(float, input().split(' '))
# if x == 0 and y == 0:
    # print("Origem")
#  x > 0 and y > 0:
    # print("Q1")
# if y > 0 > x:
    # print("Q2")
# if x < 0 and y < 0:
    # print("Q3")
# if x > 0 > y:
    # print("Q4")
# if x == 0 and y > 0:
    # print("Eixo Y")
# if x > 0 and y == 0:
    # print("Eixo X")
# if x == 0 and y < 0:
    # print("Eixo Y")
# if x < 0 and y == 0:
    # print("Eixo X")

# x, y = map(float, input().split(' '))
# if x == 0 and y == 0:
    # print("Origem")
# else:
    # if x > 0 and y > 0:
        # print("Q1")
    # else:
        # if y > 0 > x:
            # print("Q2")
        # else:
            # if x < 0 and y < 0:
                # print("Q3")
            # else:
                # if x > 0 > y:
                    # print("Q4")
                # else:
                    # if x == 0:
                        # print("Eixo Y")
                    # else:
                        # if y == 0:
                            # print("Eixo X")
