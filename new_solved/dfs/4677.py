import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(i, j):
    arr[i][j] = 1

    for k in range(8):
        y, x = i + dy[k], j + dx[k]

        if y in (-1, n) or x in (-1, m) or arr[y][x]:
            continue

        dfs(y, x)

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]
f = lambda x:-1 if x == "*" else 0

n, m = map(int, input().split())

while n:
    res = 0
    arr = [list(map(f, input().strip())) for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if not arr[i][j]:
                res += 1
                dfs(i, j)
    
    print(res)

    n, m = map(int, input().split())