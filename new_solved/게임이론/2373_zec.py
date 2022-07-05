f = [1] * 30

for i in range(28):
    f[i + 2] = f[i] + f[i + 1]

n = int(input())

if n in f:
    print(-1)
else:
    for i in range(29, 0, -1):
        if n > f[i]:
            n -= f[i]
        elif n == f[i]:
            break
    print(n)