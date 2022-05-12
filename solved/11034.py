while True:
    try:
        a, b, c = map(int, input().split())
        step = 0
        while True:
            if c - b == 1 and b - a == 1:
                break

            if c - b >= b - a:
                a, b = b, b + 1
            else:
                b, c = b - 1, b
            step += 1
        print(step)

    except EOFError:
        break