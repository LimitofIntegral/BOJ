import heapq as h
from collections import deque

dy, dx = (1, -1, 0, 0), (0, 0, 1, -1)

def bfs(i, j):
    heap, visited = [(0, i, j, -1)], {}

    while heap:
        step, ny, nx, d = h.heappop(heap)

        try:
            if visited[ny, nx] < step:
                continue
            visited[ny, nx] = step
        except:
            visited[ny, nx] = step

        for k in range(4):
            y, x = ny + dy[k], nx + dx[k]

            if y in (-1, n) or x in (-1, m) or arr[y][x] == "*":
                continue
            
            if d == -1:
                h.heappush(heap, (step, y, x, k))
            else:
                if k == d:
                    h.heappush(heap, (step, y, x, k))
                else:
                    h.heappush(heap, (step + 1, y, x, k))
    
    return visited[ey, ex]


m, n = map(int, input().split())
arr = [list(input()) for _ in range(n)]

sy, sx, ey, ex = None, None, None, None

for i in range(n):
    for j in range(m):
        if arr[i][j] == "C":
            if sy != None:
                ey, ex = i, j
                break
            else:
                sy, sx = i, j

print(bfs(sy, sx))