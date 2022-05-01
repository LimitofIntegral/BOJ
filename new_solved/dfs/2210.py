dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

def dfs(i, j, string):
    global count

    result = string + field[i][j]

    if len(result) == 6:
        if result in arr:
            return
        else:
            arr[result] = None
            count += 1
            return

    for k in range(4):
        x, y = j + dx[k], i + dy[k]
        if x < 0 or x > 4 or y < 0 or y > 4:
            continue
        dfs(y, x, result)


arr = {}
count = 0

field = [list(input().split()) for _ in range(5)]

for i in range(5):
    for j in range(5):
        dfs(i, j, "")

print(count)