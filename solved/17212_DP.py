n = int(input())

p = [i for i in range(n + 1)]
c = [0] * (n + 1)
c_ = [2, 5, 7]

for i in range(1, n + 1):
    c[i] = c[i - 1] + 1
    for j in c_:
        if i >= j:
            c[i] = min(c[i], c[i - j] + 1)

print(c[n])