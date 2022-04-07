import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    global day
    while q:
        day += 1
        for _ in range(len(q)):
            l, i, j = q.popleft()
            for p in range(6):
                x, y, z = i + dx[p], j + dy[p], l + dz[p]
                if x < 0 or x >= m or y < 0 or y >= n or z < 0 or z >= k:
                    continue
                if not box[z][x][y]:
                    box[z][x][y] = 1
                    q.append((z, x, y))

def check():
    for i in box:
        for j in i:
            for k in j:
                if not k:
                    return False
    return True

q = deque([])

dx = (0, 0, 1, -1, 0, 0)
dy = (0, 0, 0, 0, 1, -1)
dz = (1, -1, 0, 0, 0, 0)

n, m, k = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(m)] for _ in range(k)]
day = 0

for l in range(k):
    for i in range(m):
        for j in range(n):
            if box[l][i][j] == 1:
                q.append((l, i, j))

bfs()

if check():
    print(day - 1)
else:
    print(-1)

