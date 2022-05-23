dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

def dfs(i, j, si, sj, letter, bi = -1, bj = -1):
    global check

    if check:
        return

    visited[i, j] = None

    stack = []

    for k in range(4):
        y = i + dy[k]
        x = j + dx[k]

        if y in (-1, n) or x in (-1, m):
            continue
        if arr[y][x] == letter:
            if (y, x) != (bi, bj):
                if (y, x) == (si, sj):
                    check = True
                    return
                if (y, x) not in visited:
                    stack.append((y, x))
    
    while stack:
        y, x = stack.pop()
        dfs(y, x, si, sj, letter, i, j)
    
    visited.pop((i, j))
    return


n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
visited, check = {}, None

for i in range(n):
    for j in range(m):
        if (i, j) not in visited:
            dfs(i, j, i, j, arr[i][j])

print("Yes" if check else "No")