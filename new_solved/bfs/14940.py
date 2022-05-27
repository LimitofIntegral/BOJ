import sys
from collections import deque
input = sys.stdin.readline

dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

def bfs():
    q = deque([(sy, sx)])
    step = 0

    while q:
        step += 1
        for _ in range(len(q)):
            i, j = q.popleft()

            for k in range(4):
                y = i + dy[k]
                x = j + dx[k]

                if y in (-1, n) or x in (-1, m):
                    continue

                if arr[y][x]:
                    continue

                arr[y][x] = step
                q.append((y, x))


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            sy, sx = i, j
            arr[i][j] = -1
        elif arr[i][j] == 1:
            arr[i][j] = 0
        else:
            arr[i][j] = -1
    
bfs()

for i in range(n):
    for j in range(m):
        if (i, j) != (sy, sx) and not arr[i][j]:
            arr[i][j] = -1
        elif arr[i][j] == -1:
            arr[i][j] = 0

for i in arr:
    print(*i)