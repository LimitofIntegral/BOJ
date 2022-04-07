def dfs():
    check = False
    while stack:
        i, j = stack.pop()
        if (i, j) in visited:
            continue
        visited.append((i, j))
        d = field[i][j]
        for k in range(4):
            x = i + dx[k] * d
            y = j + dy[k] * d
            if x < 0 or x >= n or y < 0 or y >= n:
                continue
            if (x, y) == (n - 1, n - 1):
                check = True
                break
            else:
                stack.append((x, y))
    return check

n = int(input())
field = [list(map(int, input().split())) for _ in range(n)]

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)
stack = [(0, 0)]
visited = []

if dfs():
    print("HaruHaru")
else:
    print("Hing")