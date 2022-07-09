import sys
sys.setrecursionlimit(10**5)

def dfs(x, y, z):
    if (x, y, z) in visited:
        return
    
    visited.add((x, y, z))

    if not x:
        if z in res:
            return
        res.add(z)
    
    # 각 물병의 남은 용량
    at, bt, ct = a - x, b - y, c - z

    if at:
        if y:
            if y >= at:
                dfs(a, y - at, z)
            else:
                dfs(x + y, 0, z)
        
        if z:
            if z >= at:
                dfs(a, y, z - at)
            else:
                dfs(x + z, y, 0)
    
    if bt:
        if x:
            if x >= bt:
                dfs(x - bt, b, z)
            else:
                dfs(0, x + y, z)
        
        if z:
            if z >= bt:
                dfs(x, b, z - bt)
            else:
                dfs(x, y + z, 0)
    
    if ct:
        if x:
            if x >= ct:
                dfs(x - ct, y, c)
            else:
                dfs(0, y, z + x)
        
        if y:
            if y >= ct:
                dfs(x, y - ct, c)
            else:
                dfs(x, 0, z + y)


a, b, c = map(int, input().split())
res = set()
visited = set()

dfs(0, 0, c)

print(*sorted(list(res)))