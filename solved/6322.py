a, b, c = map(int, input().split())

i = 1
while a and b and c:
    print(f'Triangle #{i}')
    i += 1
    if c == -1:
        print("c = " + "{:.3f}".format((a**2 + b**2) ** 0.5))
    else:
        if a == -1:
            if b >= c:
                print("Impossible.")
            else:
                print("a = " + "{:.3f}".format((c**2 - b**2) ** 0.5))
        else:
            if a >= c:
                print("Impossible.")
            else:
                print("b = " + "{:.3f}".format((c**2 - a**2) ** 0.5))
    print()

    a, b, c = map(int, input().split())
