visited = []
stack = []
result = 0

n, m = map(int, input().split())
field = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if (i, j) in visited:
            continue
        result += 1
        visited.append((i, j))
        x = j
        y = i
        if field[i][j] == '-':
            while True:
                x += 1
                if x >= m:
                    break
                if field[i][x] == '-':
                    visited.append((i, x))
                else:
                    break
        else:
            while True:
                y += 1
                if y >= n:
                    break
                if field[y][j] == '|':
                    visited.append((y, j))
                else:
                    break

print(result)