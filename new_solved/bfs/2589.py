from collections import deque
import sys
input = sys.stdin.readline

dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

def bfs(i, j):
    if field[i][j] == "W":
        return 0
    visited = {}
    q.append((i, j))
    step = -1

    while q:
        step += 1
        for _ in range(len(q)):
            y_, x_ = q.popleft()
            if (y_, x_) in visited:
                continue
            visited[y_, x_] = None
            for k in range(4):
                y, x = y_ + dy[k], x_ + dx[k]
                if y < 0 or y >= n or x < 0 or x >= m:
                    continue
                if (y, x) in visited:
                    continue
                if field[y][x] == "L":
                    q.append((y, x))

    return step


n, m = map(int, input().split())
field = [list(input()) for _ in range(n)]
q = deque([])
result = 0

for i in range(n):
    for j in range(m):
        result = max(result, bfs(i, j))

print(result)