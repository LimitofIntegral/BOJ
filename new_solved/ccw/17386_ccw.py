def CCW(p1, p2, p3):
    a = p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1]
    b = p1[1] * p2[0] + p2[1] * p3[0] + p3[1] * p1[0]

    if a - b > 0:
        return 1
    elif a - b < 0:
        return -1
    else:
        return 0
        

a, b, c, d = map(int, input().split())
p1 = [a, b]
p2 = [c, d]
a, b, c, d = map(int, input().split())
p3 = [a, b]
p4 = [c, d]

r1 = CCW(p1, p2, p3) * CCW(p1, p2, p4)
r2 = CCW(p3, p4, p1) * CCW(p3, p4, p2)

if (r1, r2) == (-1, -1):
    print(1)
else:
    print(0)