import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = (0, 1)
dy = (1, 0)

def dfs(i, j, t):
    global M, m
    if (i, j) == (n - 1, n - 1):
        M, m = max(M, int(t)), min(m, int(t))
        return
    
    for k in range(2):
        y = i + dy[k]
        x = j + dx[k]
        if y >= n or x >= n:
            continue
        p = arr[y][x]
        if p in ("+", "-", "*"):
            dfs(y, x, t + p)
        else:
            dfs(y, x, str(eval(t + p)))
    
    return


M, m = -float('inf'), float('inf')
n = int(input())
arr = [list(input().split()) for _ in range(n)]

dfs(0, 0, arr[0][0])

print(M, m)