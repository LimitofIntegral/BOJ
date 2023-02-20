import sys
from collections import deque
input = sys.stdin.readline

def dfs(now):
    if now in visited:
        res.append(now)
        return ' to '.join(res)
    res.append(now)
    visited.add(now)

    return dfs(G[now])

case = 1

while True:
    q = deque()
    G = {}
    visited = set()

    while t:=list(input().split()):
        if len(t) == 1:
            break
        q.append(t[0])
        G[t[0]] = t[1]

    if not q:
        break
    
    if case > 1:
        print()
    
    print(f'Party number {case}')
    case += 1

    while q:
        now = q.popleft()

        if now in visited:
            continue
        
        res = []

        print(dfs(now) + ".")
