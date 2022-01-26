from re import M


n, m = map(int, input().split())
box = 1

if n == 0:
    print(0)
else:
    b = list(map(int, input().split()))
    w = m
    for i in b:
        if w >= i:
            w -= i
        else:
            box += 1
            w = m - i
    print(box)