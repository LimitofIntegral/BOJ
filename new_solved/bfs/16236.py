from collections import deque
import heapq as h

dy, dx = (1, -1, 0, 0), (0, 0, 1, -1)

def bfs(i, j, size):
    q, heap, visited = deque([(i, j)]), [], {}
    step = 0

    while q:
        step += 1
        for _ in range(len(q)):
            ny, nx = q.popleft()

            if (ny, nx) in visited:
                continue

            visited[ny, nx] = None

            for k in range(4):
                y, x = ny + dy[k], nx + dx[k]

                if y in (-1, n) or x in (-1, n) or (y, x) in visited:
                    continue

                if arr[y][x] > size:
                    continue
                    
                q.append((y, x))

                if arr[y][x] and arr[y][x] < size:
                    h.heappush(heap, (step, y, x))
        if heap:
            return heap[0]
    
    return None


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
size, count = 2, 0

for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            s_y, s_x = i, j
            arr[i][j] = 0
            break

res = 0
to = bfs(s_y, s_x, size)

while to:
    res += to[0]
    s_y, s_x = to[1], to[2]
    arr[s_y][s_x] = 0

    count += 1

    if size == count:
        size += 1
        count = 0
    
    to = bfs(s_y, s_x, size)

print(res)