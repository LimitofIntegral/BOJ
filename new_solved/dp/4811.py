def dfs(a, b, w = 0):
    if (a, b) in dp:
        return dp[a, b]
    
    if a:
        w += dfs(a - 1, b + 1)
    if b:
        w += dfs(a, b - 1)
    
    dp[a, b] = w
    return dp[a, b]

result, dp = 0, {(0, 0) : 1}

n = int(input())
while n:
    print(dfs(n, 0))
    n = int(input())