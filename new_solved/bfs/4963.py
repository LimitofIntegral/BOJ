from collections import deque

def bfs(i, j):
    q = deque([(i, j)])

    while q:
        y_, x_ = q.popleft()
        if visited[y_][x_]:
            continue
        visited[y_][x_] = True
        for k in range(8):
            x = x_ + dx[k]
            y = y_ + dy[k]
            if x < 0 or x >= c or y < 0 or y >= r:
                continue
            if field[y][x]:
                q.append((y, x))


dx = (1, 1, 0, -1, -1, -1, 0, 1)
dy = (0, -1, -1, -1, 0, 1, 1, 1)

c, r = map(int, input().split())

while c and r:
    result = 0
    field = [list(map(int, input().split())) for _ in range(r)]
    visited = [[False] * c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if field[i][j] and not visited[i][j]:
                result += 1
                bfs(i, j)

    print(result)

    c, r = map(int, input().split())