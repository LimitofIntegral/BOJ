import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

def dfs(i, j, a, b):
    global temp
    arr[i][j] = 0
    temp += 1

    for k in range(4):
        y = i + dy[k]
        x = j + dx[k]

        if y < 0 or y >= n or x < 0 or x >= m:
            continue
        if (y, x) == (a, b):
            continue
        if arr[y][x]:
            dfs(y, x, i, j)
    
    return

result = 0
n, m, k = map(int, input().split())
arr = [[0] * m for _ in range(n)]

for _ in range(k):
    y, x = map(int, input().split())
    arr[y - 1][x - 1] = 1

for i in range(n):
    for j in range(m):
        if arr[i][j]:
            temp = 0
            dfs(i, j, -1, -1)
            result = max(result, temp)

print(result)