while True:
    try:
        v, t = map(int, input().split())
        r = (v * 2) * t
        print(r)
    except EOFError:
        break