import sys
from collections import deque
input = sys.stdin.readline

def dfs(y_, x_, number, v):
    if y_ == n - 1:
        return number
    
    temp = None

    for k in range(4):
        y, x = y_ + dy[k], x_ + dx[k]

        if y in (-1, n) or x in (-1, m) or (y, x) in v or a[y][x] not in number:
            continue
        
        v.add((y, x))
        temp = dfs(y, x, number, v)
        v.remove((y, x))

        if temp:
            return temp
    
    return None

def bfs(y_, x_, number):
    v = set()
    q = deque([(y_, x_)])

    while q:
        y_, x_ = q.popleft()

        for k in range(4):
            y, x = y_ + dy[k], x_ + dx[k]

            if y in (-1, n) or x in (-1, m) or (y, x) in v or a[y][x] not in number:
                continue
            
            if y == n - 1:
                return number

            v.add((y, x))
            q.append((y, x))
    
    return None


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

for i in range(10):
    for j in range(10):
        for k in range(10):
            for row in range(m):
                if a[0][row] not in (i, j, k):
                    continue
                res = bfs(0, row, (i, j, k))
                if res:
                    print(*res)
                    sys.exit()

print(-1, -1, -1)