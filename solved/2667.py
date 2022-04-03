def search(i, j):
    global count
    if (i, j) not in visited:
        visited.append((i, j))
        if field[i][j]:
            count += 1
            for k in range(4):
                x = i + dx[k]
                if x < 0 or x >= n:
                    continue
                y = j + dy[k]
                if y < 0 or y >= n:
                    continue
                search(x, y)
    else:
        return

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

n = int(input())
count = 0
cnt = []
field = []
visited = []

for _ in range(n):
    field.append(list(map(int, list(input()))))

for i in range(n):
    for j in range(n):
        count = 0
        search(i, j)
        if count:
            cnt.append(count)

cnt.sort()

print(len(cnt))
for i in cnt:
    print(i)