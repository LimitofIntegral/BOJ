import sys
sys.setrecursionlimit(10**6)

dx = (1, -1, 0, 0)
dy = (0, 0, -1, 1)

def dfs(i, j, step, P, visited = {}):
    global total
    visited[i, j] = None

    if step == m:
        total += P
        visited.pop((i, j))
        return

    for k in range(4):
        y = i + dy[k]
        x = j + dx[k]

        if (y, x) in visited:
            continue

        dfs(y, x, step + 1, P * arr[k] / 100, visited)
    
    visited.pop((i, j))
    return


m, E, W, S, N = map(int, input().split())
arr = [E, W, S, N]

total = 0

dfs(0, 0, 0, 1)

print(total)