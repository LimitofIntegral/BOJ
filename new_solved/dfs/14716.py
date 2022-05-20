import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = (1, 1, 0, -1, -1, -1, 0, 1)
dy = (0, 1, 1, 1, 0, -1, -1, -1)

def dfs(i, j, a, b):
    arr[i][j] = 0

    for k in range(8):
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
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j]:
            result += 1
            dfs(i, j, -1, -1)

print(result)