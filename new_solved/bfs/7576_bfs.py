import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    global day
    while q:
        day += 1
        for _ in range(len(q)):
            i, j = q.popleft()
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if x < 0 or x >= m or y < 0 or y >= n:
                    continue
                if not box[x][y]:
                    box[x][y] = 1
                    q.append((x, y))

def check():
    for i in box:
        for j in i:
            if not j:
                return False
    return True

q = deque([])

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

n, m = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(m)]
day = 0

for i in range(m):
    for j in range(n):
        if box[i][j] == 1:
            q.append((i, j))

bfs()

if check():
    print(day - 1)
else:
    print(-1)

