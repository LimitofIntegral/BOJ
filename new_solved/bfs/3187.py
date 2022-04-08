from collections import deque
import sys
input = sys.stdin.readline

def bfs(i, j):
    q = deque([(i, j)])
    s, w = 0, 0
    while q:
        y_, x_ = q.popleft()
        if field[y_][x_] == "#" or visited[y_][x_]:
            continue
        visited[y_][x_] = True
        if field[y_][x_] == "v":
            w += 1
        if field[y_][x_] == "k":
            s += 1
        for k in range(4):
            x = x_ + dx[k]
            y = y_ + dy[k]
            if x < 0 or x >= c or y < 0 or y >= r:
                continue
            q.append((y, x))
    
    if s > w:
        return s, 0
    else:
        return 0, w


dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

q = deque([])
sheep, wolf = 0, 0

r, c = map(int, input().split())
visited = [[False] * c for _ in range(r)]
field = [list(input()) for _ in range(r)]

for i in range(r):
    for j in range(c):
        if visited[i][j]:
            continue
        result = bfs(i, j)
        sheep += result[0]
        wolf += result[1]

print(sheep, wolf)