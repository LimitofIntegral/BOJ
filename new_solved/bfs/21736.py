from collections import deque
import sys
input = sys.stdin.readline

dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

def bfs(i, j):
    q = deque([(i, j)])
    result = 0

    while q:
        y_, x_ = q.popleft()
        if (y_, x_) in visited:
            continue
        visited[y_, x_] = None
        if field[y_][x_] == "P":
            result += 1
        for k in range(4):
            y, x = y_ + dy[k], x_ + dx[k]
            if y < 0 or y >= n or x < 0 or x >= m:
                continue
            if field[y][x] == "X":
                continue
            q.append((y, x))

    return result
    

n, m = map(int, input().split())
field = [list(input().strip()) for _ in range(n)]
visited = {}


for i in range(n):
    for j in range(m):
        if field[i][j] == "I":
            y, x = i, j
            break

result = bfs(y, x)

print(result if result else "TT")