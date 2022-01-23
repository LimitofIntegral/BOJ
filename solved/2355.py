def s(a, b):
    t = (b - a + 1) // 2
    if (b - a) % 2:
        return (b + a) * t
    else:
        return (b + a) * t + int((b + a) / 2)

a, b = map(int, input().split())

if a > b:
    a, b = b, a

print(s(a, b))