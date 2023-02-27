import sys
from collections import deque
input = sys.stdin.readline

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

res = 0
q = deque()
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

Max = max([max(i) for i in a])

for rain in range(Max + 1):
    visited = [[False] * n for _ in range(n)]
    temp = 0

    for i in range(n):
        for j in range(n):
            if a[i][j] - rain > 0 and not visited[i][j]:
                q.append((i, j))
                visited[i][j] = True
                temp += 1
                while q:
                    y_, x_ = q.popleft()

                    for k in range(4):
                        y, x = y_ + dy[k], x_ + dx[k]

                        if y in (-1, n) or x in (-1, n) or visited[y][x]:
                            continue
                        
                        if a[y][x] - rain > 0:
                            q.append((y, x))
                            visited[y][x] = True

    res = max(res, temp)

print(res)
