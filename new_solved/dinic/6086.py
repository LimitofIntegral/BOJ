import sys
from collections import deque
sys.setrecursionlimit(10**4)
d = lambda x: ord(x) - 65 if "A" <= x <= "Z" else ord(x) - 71

def bfs():
    level = [-1] * 52
    level[0] = 0
    q = deque([0])

    while q:
        now = q.popleft()
        for to in adj[now]:
            if level[to] == -1 and c[now][to] - f[now][to] > 0:
                level[to] = level[now] + 1
                q.append(to)

    return level if level[25] != -1 else []


def dfs(now, flow):
    if now == 25:
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
n = int(input())
c = {i : {} for i in range(52)}
f = {i : {} for i in range(52)}
adj = {i : [] for i in range(52)}

for _ in range(n):
    a, b, w = input().split()
    a, b, w = d(a), d(b), int(w)
    
    if b in c[a]:
        c[a][b] += w
        c[b][a] += w
    else:
        c[a][b], f[a][b] = w, 0
        c[b][a], f[b][a] = w, 0
        adj[a].append(b)
        adj[b].append(a)

level = bfs()

while level:
    while True:
        flow = dfs(0, float('inf'))
        if not flow:
            break
        res += flow
    level = bfs()

print(res)
