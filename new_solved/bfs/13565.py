import sys
from collections import deque
input = sys.stdin.readline

dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

def bfs(i, j):
    q = deque([(i, j)])

    while q:
        y_, x_ = q.popleft()
        if (y_, x_) not in visited:
            visited[(y_, x_)] = None

            for k in range(4):
                y = y_ + dy[k]
                x = x_ + dx[k]
                if x < 0 or x >= m or y < 0 or y >= n:
                    continue

                if y == n - 1:
                    return True    
                
                if field[y][x] == "0":
                    q.append((y, x))

    return False


visited = {}

n, m = map(int, input().split())

field = [list(input()) for _ in range(n)]

result = False

for j in range(m):
    if field[0][j] == "0":
        result = bfs(0, j)
        if result:
            break

if result:
    print("YES")
else:
    print("NO")
