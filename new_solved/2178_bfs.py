from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    global day
    while q:
        day += 1
        for _ in range(len(q)):
            i, j = q.popleft()
            for k in range(4):
                x, y = i + dx[k], j + dy[k]
                if x < 0 or x >= n or y < 0 or y >= m:
                    continue
                if (x, y) not in visited:
                    visited.append((x, y))
                    if field[x][y] == "1":
                        if (x, y) == (n - 1, m - 1):
                            day += 1
                            return
                        q.append((x, y))

q = deque([(0, 0)])

n, m = map(int, input().split())
dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)
day = 0

field = []
visited = []

for _ in range(n):
    field.append(list(input()))

bfs()

print(day)