a, b = map(int, input().split())

while a and b:
    t = int(a ** (1 / b))
    if a - t ** b > (t + 1) ** b - a:
        print(t + 1)
    else:
        print(t)
    a, b = map(int, input().split())
