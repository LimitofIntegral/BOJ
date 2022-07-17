import sys
sys.setrecursionlimit(10**5)

dy, dx = (1, -1, 0, 0), (0, 0, 1, -1)

def b_move(by, bx, ry, rx, k):
    i, j = by, bx
    while True:
        y, x = i + dy[k], j + dx[k]
        if arr[y][x] == "O":
            return 0, 0

        if arr[y][x] == "#" or (y, x) == (ry, rx):
            break
        i, j = y, x
    
    return i, j


def r_move(ry, rx, by, bx, k):
    i, j = ry, rx
    while True:
        y, x = i + dy[k], j + dx[k]
        if arr[y][x] == "O":
            return 0, 0

        if arr[y][x] == "#" or (y, x) == (by, bx):
            break
        i, j = y, x
    
    return i, j


def dfs(b_y, b_x, r_y, r_x, step=0):
    if step == 10:
        return False
    res = False

    for k in range(4):
        if k == 0:
            if b_y < r_y:
                ry, rx = r_move(r_y, r_x, b_y, b_x, k)
                by, bx = b_move(b_y, b_x, ry, rx, k)
            else:
                by, bx = b_move(b_y, b_x, r_y, r_x, k)
                ry, rx = r_move(r_y, r_x, by, bx, k)
        elif k == 1:
            if b_y > r_y:
                ry, rx = r_move(r_y, r_x, b_y, b_x, k)
                by, bx = b_move(b_y, b_x, ry, rx, k)
            else:
                by, bx = b_move(b_y, b_x, r_y, r_x, k)
                ry, rx = r_move(r_y, r_x, by, bx, k)
        elif k == 2:
            if b_x < r_x:
                ry, rx = r_move(r_y, r_x, b_y, b_x, k)
                by, bx = b_move(b_y, b_x, ry, rx, k)
            else:
                by, bx = b_move(b_y, b_x, r_y, r_x, k)
                ry, rx = r_move(r_y, r_x, by, bx, k)
        else:
            if b_x > r_x:
                ry, rx = r_move(r_y, r_x, b_y, b_x, k)
                by, bx = b_move(b_y, b_x, ry, rx, k)
            else:
                by, bx = b_move(b_y, b_x, r_y, r_x, k)
                ry, rx = r_move(r_y, r_x, by, bx, k)
        
        if not ry and by:
            return True
        
        res = res or dfs(by, bx, ry, rx, step + 1)

        if res:
            return True


n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

b_y, b_x, r_y, r_x = None, None, None, None

for i in range(n):
    for j in range(m):
        if arr[i][j] == "B":
            arr[i][j] = "."
            b_y, b_x = i, j
            if b_y and r_y:
                break
        if arr[i][j] == "R":
            arr[i][j] = "."
            r_y, r_x = i, j
            if b_y and r_y:
                break

print(1 if dfs(b_y, b_x, r_y, r_x) else 0)