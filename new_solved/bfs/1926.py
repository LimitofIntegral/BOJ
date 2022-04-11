from collections import deque

dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)
size = []

n, m = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]

q = deque([])
visited = {(i, j) : True for i in range(n) for j in range(m)}

for i in range(n):
    for j in range(m):
        size_ = 0
        if visited[(i, j)]:
            if field[i][j]:
                q.append((i, j))

            while q:
                y_, x_ = q.popleft()
                if visited[(y_, x_)]:
                    size_ += 1
                    visited[(y_, x_)] = False
                    for k in range(4):
                        x = x_ + dx[k]
                        y = y_ + dy[k]
                        if x < 0 or x >= m or y < 0  or y >= n:
                            continue
                        if field[y][x]:
                            q.append((y, x))
            
        if size_:
            size.append(size_)

if size:
    print(len(size))
    print(max(size))
else:
    print(0)
    print(0)

