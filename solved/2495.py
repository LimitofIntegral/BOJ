for _ in range(3):
    t = list(input())
    r, c, p = 1, 1, t[0]
    for i in range(1, 8):
        if p == t[i]:
            c += 1
        else:
            r, c, p = max(r, c), 1, t[i]
    print(max(r, c))
    