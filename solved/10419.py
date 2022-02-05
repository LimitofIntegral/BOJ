for _ in range(int(input())):
    d = int(input())
    s, t = 0, 0
    while s + t <= d:
        t += 1
        s = t ** 2
    print(t - 1)