from collections import deque

def bfs(i, j):
    q = deque([])
    result = 0
    if (i, j) not in visited:
        q.append((i, j))
        while q:
            y_, x_ = q.popleft()
            if (y_, x_) in visited:
                continue
            visited.append((y_, x_))
            result += 1
            for d in range(4):
                y = y_ + dy[d]
                x = x_ + dx[d]
                if x < 0 or x >= m or y < 0 or y >= n:
                    continue
                if field[y][x]:
                    q.append((y, x))
    return result


dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

n, m, k = map(int, input().split())

field = [[1] * m for _ in range(n)]

for _ in range(k):
    x1, y1, x2, y2 = map(int,input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            field[i][j] = 0

visited = []
arr = []

for i in range(n):
    for j in range(m):
        if field[i][j]:
            temp = bfs(i, j)
            if temp:
                arr.append(temp)

arr.sort()

print(len(arr))
for i in arr:
    print(i, end = " ")
