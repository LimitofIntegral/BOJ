import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    level = [-1] * (n + 1)
    level[1] = 0
    q = deque([1])

    while q:
        now = q.popleft()
        for to in adj[now]:
            if level[to] == -1 and c[now][to] - f[now][to] > 0:
                level[to] = level[now] + 1
                q.append(to)
    
    return level if level[2] != -1 else []


def dfs(now, flow):
    if now == 2:
        return flow
    
    for to in adj[now]:
        t = c[now][to] - f[now][to]
        if level[to] == level[now] + 1 and t > 0:
            r = dfs(to, min(t, flow))

            if r > 0:
                f[now][to] += r
                f[to][now] -= r

                return r
    
    return 0


res = 0
n, p = map(int, input().split())
c = {i + 1 : {} for i in range(n)}
f = {i + 1 : {} for i in range(n)}
adj = {i + 1 : [] for i in range(n)}

for _ in range(p):
    a, b = map(int, input().split())

    if b in c[a]:
        c[a][b] += 1
    else:
        c[a][b] = 1
        c[b][a] = 0
        f[a][b] = 0
        f[b][a] = 0
        adj[a].append(b)
        adj[b].append(a)
    
level = bfs()

while level:
    while True:
        flow = dfs(1, float('inf'))
        if not flow:
            break
        res += flow
    level = bfs()

print(res)