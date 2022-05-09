import sys
sys.setrecursionlimit(10 ** 6)

dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

def dfs(i, j):
    if (i, j) in visited:
        return False
    visited[i, j] = None
    
    if not field[i][j]:
        return False
    
    while True:
        for k in range(4):
            y, x = i + dy[k], j + dx[k]
            if y < 0 or y >= n or x < 0 or x >= m:
                continue
            dfs(y, x)
        return True


visited, result = {}, 0
n, m = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]
t = int(input())

for i in range(n):
    for j in range(m):
        if sum(field[i][j * 3:(j + 1) * 3]) / 3 >= t:
            field[i][j] = 255
        else:
            field[i][j] = 0


for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print(result)