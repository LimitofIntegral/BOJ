n = int(input())
a = [i for i in range(1, n + 1)]

t = 1
while len(a) > 1:
    p = t**3 % len(a) - 1
    if p == -1:
        p = len(a) - 1
    t += 1
    a = a[p+1:] + a[:p]

print(a[0])
