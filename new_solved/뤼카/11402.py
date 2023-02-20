n, k, m = map(int, input().split())

dp = [[0] * 2001 for _ in range(2001)]

for i in range(m):
    dp[i][0] = 1
    for j in range(1, i + 1):
        dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % m
    
res = 1
while n or k:
    res *= dp[n % m][k % m]
    n //= m
    k //= m
    res %= m

print(res)