for _ in range(int(input())):
    c, g = 0, 0
    for _ in range(int(input())):
        a, b = map(float, input().split())
        c += int(a)
        g += a * b
    print(c, round(g / c, 1))