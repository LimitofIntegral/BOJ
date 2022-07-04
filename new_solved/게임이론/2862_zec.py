f = [0] * 73
f[0], f[1] = 1, 1

for i in range(71):
    f[i + 2] = f[i] + f[i + 1]

n = int(input())

for i in range(72, 0, -1):
    if n > f[i]:
        n -= f[i]
    elif n == f[i]:
        print(n)
        break
