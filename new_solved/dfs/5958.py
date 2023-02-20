import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(i, j):
    arr[i][j] = 1

    for k in range(4):
        y, x = i + dy[k], j + dx[k]

        if y in (-1, n) or x in (-1, n) or arr[y][x]:
            continue

        dfs(y, x)

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

f = lambda x:0 if x == "*" else -1
res = 0

n = int(input())
arr = [list(map(f, input().strip())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not arr[i][j]:
            res += 1
            dfs(i, j)

print(res)