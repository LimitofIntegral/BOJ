import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
s = sum(a)
a *= 2
res, temp = 0, 0
for i in range(1, n + 1):
    t = 0
    for j in range(i, i + n):
        t += a[j]
        if t < 0:
            temp = -t
            res += (temp - 1)//s + 1

print(res)