dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

def dfs(i, j):
    global result
    p = ord(arr[i][j]) - 65

    visited[p] = 1

    stack = []

    for k in range(4):
        y = i + dy[k]
        x = j + dx[k]

        if y in (-1, r) or x in (-1, c):
            continue
        if not visited[ord(arr[y][x]) - 65]:
            stack.append((y, x))

    if not stack:
        result = max(result, sum(visited))
        visited[p] = 0
        return
    
    while stack:
        y, x = stack.pop()
        dfs(y, x)
    
    visited[p] = 0
    return

r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
visited = [0] * 26
result = 1
dfs(0, 0)
print(result)