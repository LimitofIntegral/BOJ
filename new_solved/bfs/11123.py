from collections import deque

dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)


def bfs(i, j):
    q = deque([(i, j)])

    while q:
        y_, x_ = q.popleft()
        if (y_, x_) in visited:
            continue
        visited[y_, x_] = None
        for k in range(4):
            y, x = y_ + dy[k], x_ + dx[k]
            if y < 0 or y >= n or x < 0 or x >= m:
                continue
            if field[y][x] == "#":
                q.append((y, x))

for _ in range(int(input())):
    n, m = map(int, input().split())
    field = [list(input()) for _ in range(n)]
    visited, count = {}, 0

    for i in range(n):
        for j in range(m):
            if field[i][j] == "#" and (i, j) not in visited:
                count += 1
                bfs(i, j)

    print(count)