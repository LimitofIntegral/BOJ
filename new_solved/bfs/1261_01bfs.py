import sys
from collections import deque
input = sys.stdin.readline

dy, dx = (1, -1, 0, 0), (0, 0, 1, -1)

visited = set()
m, n = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]

q = deque([(0, 0, 0)])

while True:
    step, i, j = q.popleft()

    if (i, j) == (n - 1, m - 1):
        print(step)
        break

    for k in range(4):
        y, x = i + dy[k], j + dx[k]

        if y in (-1, n) or x in (-1, m) or (y, x) in visited:
            continue
        
        visited.add((y, x))

        if arr[y][x] == "0":
            q.appendleft((step, y, x))
        else:
            q.append((step + 1, y, x))
