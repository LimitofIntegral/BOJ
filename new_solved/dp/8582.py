import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)
dp2 = [0] * (n + 2)
a = [0] + [int(input()) for _ in range(n)]

for i in range(1, n + 1):
    dp[i] = max(a[i], dp[i - 1])

for i in range(n, 0, -1):
    dp2[i] = max(a[i], dp2[i + 1])

for i in range(1, n + 1):
    print(dp[i], dp2[i])