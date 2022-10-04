import sys
input = sys.stdin.readline

n = int(input())
dp = [[0] * (n + 2) for _ in range(n + 2)]
m = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(1, n - i + 1):
        dp[j][i + j] = float('inf')
        for k in range(j, i + j + 1):
            dp[j][i + j] = min(dp[j][i + j], dp[j][k] + dp[k + 1][i + j] + m[j][0] * m[k][1] * m[i+j][1])

print(dp[1][n])