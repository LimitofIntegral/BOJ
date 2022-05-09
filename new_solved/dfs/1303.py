dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

def dfs(i, j, color):
    if (i, j) in visited:
        return 0
    size = 1
    visited[i, j] = None
    for k in range(4):
        y, x = i + dy[k], j + dx[k]
        if y < 0 or y >= n or x < 0 or x >= m:
            continue
        if field[y][x] == color:
            size += dfs(y, x, color)
    return size


m, n = map(int, input().split())
field = [list(input()) for _ in range(n)]
visited, result = {}, {'W' : [], 'B' : []}

for i in range(n):
    for j in range(m):
        color = field[i][j]
        temp = dfs(i, j, color)
        if temp:
            result[color].append(temp)

print(sum([i ** 2 for i in result['W']]), sum([i ** 2 for i in result['B']]))