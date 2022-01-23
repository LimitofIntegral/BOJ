def fact(n):
    if n == 1:
        return 1
    else:
        res = 1
        while n != 1:
            res *= n
            n -= 1
        
        return res

f = [1]
for i in range(0, 1000001):
    f += [f[i] * (i + 2)]

def calc(n, m):
    if n == 0 or m == 0:
        return 1
    else:
        res = (fact(n + m) / fact(n)) / fact(m)
        return res


n = int(input())

arr = [(n - i * 2, i) for i in range(n // 2 + 1)]

res = 0

for i in arr:
    res += calc(i[0], i[1])

print(int(res))