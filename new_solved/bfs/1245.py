import sys
from collections import deque
input = sys.stdin.readline

dy = (1, -1, 0, 0, 1, 1, -1, -1)
dx = (0, 0, 1, -1, 1, -1, -1, 1)

def bfs(i, j):
    q = deque([(i, j)])

    while q:
        for _ in range(len(q)):
            i, j = q.popleft()

            temp[i][j] = 0

            for k in range(8):
                y = i + dy[k]
                x = j + dx[k]

                if y in (-1, n) or x in (-1, m) or not temp[y][x]:
                    continue
                
                q.append((y, x))
                


def check(i, j, visited = {}):
    r = True
    visited[i, j] = None

    for k in range(8):
        y = i + dy[k]
        x = j + dx[k]

        if y in (-1, n) or x in (-1, m):
            continue

        if (y, x) in visited:
            continue

        if arr[y][x] == 0:
            continue

        if arr[y][x] > arr[i][j]:
            visited.pop((i, j))
            return False
        elif arr[y][x] == arr[i][j]:
            r = r and check(y, x, visited)
    
        if not r:
            visited.pop((i, j))
            return r

    visited.pop((i, j))
    return r


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
temp = [[0] * m for _ in range(n)]
r = 0

for i in range(n):
    for j in range(m):
        if check(i, j):
            temp[i][j] = 1

for i in range(n):
    for j in range(m):
        if temp[i][j]:
            bfs(i, j)
            r += 1

print(r)
