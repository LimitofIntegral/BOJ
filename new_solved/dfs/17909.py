import sys
sys.setrecursionlimit(260000)
input = sys.stdin.readline

d = {"U" : (-1, 0), "D" : (1, 0), "L" : (0, -1), "R" : (0, 1)}

def dfs(i, j):
    y, x = i + d[a[i][j]][0], j + d[a[i][j]][1]

    if y in (-1, n) or x in (-1, m):
        a[i][j] = "Y"
        return
    
    if a[y][x] not in ("U", "D", "L", "R"):
        a[i][j] = a[y][x]
        return
    
    if (i, j) in visited:
        a[i][j] = "N"
        return
    
    visited[i, j] = None
    dfs(y, x)
    a[i][j] = a[y][x]
    return


n, m = map(int, input().split())
a = [list(input().strip()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if a[i][j] in ("U", "D", "L", "R"):
            visited = {}
            dfs(i, j)

result = 0

for i in a:
    for j in i:
        if j == "Y":
            result += 1

print(result)