import sys
input = sys.stdin.readline

dy, dx = (-1, 0, 1, 0), (0, -1, 0, 1)

def find(arr):
    item = []
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                item.append((i, j, arr[i][j]))
    
    return item


def M(arr):
    res = 0
    for i in range(n):
        for j in range(n):
            res = max(res, arr[i][j])
    
    return res


def move(item, k):
    temp = [[0] * n for _ in range(n)]
    check = set()

    for a in item:
        i, j, v = a

        if k == 0:
            if i == 0:
                temp[i][j] = v
                continue
        
        if k == 1:
            if j == 0:
                temp[i][j] = v
                continue

        if k == 2:
            if i == n - 1:
                temp[i][j] = v
                continue
        
        if k == 3:
            if j == n - 1:
                temp[i][j] = v
                continue

        while True:
            y, x = i + dy[k], j + dx[k]

            if temp[y][x]:
                if temp[y][x] == v and (y, x) not in check:
                    temp[y][x] += v
                    check.add((y, x))
                else:
                    temp[i][j] = v
                break
            else:
                if k == 0 and y == 0:
                    temp[y][x] = v
                    break
                elif k == 1 and x == 0:
                    temp[y][x] = v
                    break
                elif k == 2 and y == n - 1:
                    temp[y][x] = v
                    break
                elif k == 3 and x == n - 1:
                    temp[y][x] = v
                    break
                else:
                    i, j = y, x

    return temp


def dfs(arr, step=0):
    if step == 5:
        return M(arr)

    res = 0
    item = find(arr)
    item_r = sorted(item, reverse=True)

    for k in range(4):
        if k < 2:
            res = max(res, dfs(move(item, k), step + 1))
        else:
            res = max(res, dfs(move(item_r, k), step + 1))

    return res


n = int(input())
field = [list(map(int, input().strip().split())) for _ in range(n)]

print(dfs(field))