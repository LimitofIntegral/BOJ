from collections import deque

def bfs(i, j):
    q = deque([(i, j)])
    count = 0
    visited = []

    while q:
        count += 1
        for _ in range(len(q)):
            a, b = q.popleft()
            if (a, b) in visited:
                continue
            visited.append((a, b))

            for k in range(4):
                y = a + dy[k]
                x = b + dx[k]
                if x < 0 or x >= m or y < 0 or y >= n:
                    continue
                if field[y][x] == "X":
                    continue
                else:
                    if field[y][x] == "G":
                        return True, count
                    else:
                        q.append((y, x))
    
    return False, -1


dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

for _ in range(int(input())):
    n, m = map(int, input().split())
    field = [list(input()) for _ in range(n)]

    sy, sx = 0, 0
    for i in range(n):
        for j in range(m):
            if field[i][j] == "S":
                sy, sx = i, j
                break
        
    result = bfs(sy, sx)
    if result[0]:
        print("Shortest Path:", result[1])
    else:
        print("No Exit")
