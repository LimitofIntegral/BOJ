import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

def dfs(i, j):
    global answer
    check = False
    step = 1
    for k in range(4):
        result = 1
        y = i + dy[k]
        x = j + dx[k]

        if y in (-1, n) or x in (-1, n):
            continue
        if arr[y][x] <= arr[i][j]:
            continue

        check = True

        if dp[y][x] != 1:
            result += dp[y][x]
        else:
            result += dfs(y, x)
        
        step = max(step, result)
    
    answer = max(answer, step)
    if check:
        dp[i][j] = step
        return step
    else:
        return 1
        

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[1] * n for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(n):
        dfs(i, j)

print(answer)