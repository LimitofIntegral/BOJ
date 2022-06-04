import sys
sys.setrecursionlimit(10**6)

dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

def dfs(i, j, b_y=0, b_x=0):
    global result
    exist = False
    visited.add((i, j))

    for k in range(4):
        y, x = i + dy[k], j + dx[k]

        if y in (0, m - 1) or x in (0, n - 1):
            continue
            
        if arr[y][x] == "#":
            continue
        
        if arr[y][x] == "T":
            exist = True
            break
    
    if arr[i][j] == "G":
        result += 1
        arr[i][j] = "."
    
    if exist:
        return
    
    for k in range(4):
        y, x = i + dy[k], j + dx[k]

        if y in (0, m - 1) or x in (0, n - 1):
            continue
        if arr[y][x] == "#" or (y, x) == (b_y, b_x):
            continue
        
        if (y, x) not in visited:
            dfs(y, x, i, j)
        
    return


n, m = map(int, input().split())
arr = [list(input()) for _ in range(m)]
visited = set()

for i in range(m):
    for j in range(n):
        if arr[i][j] == "P":
            s_y, s_x = i, j
            break

result = 0
dfs(s_y, s_x)
print(result)