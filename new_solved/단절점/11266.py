import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(now, root):
    global step
    d[now] = step
    step += 1

    ret = d[now]
    child = 0

    for to in graph[now]:
        if d[to]:
            ret = min(ret, d[to])
            continue
        child += 1
        prev = dfs(to, False)

        if not root and prev >= d[now]:
            C[now] = True
        
        ret = min(ret, prev)
    
    if root:
        C[now] = (child >= 2)
    
    return ret


d = [0] * 10002
C = [0] * 10002
step = 1

v, e = map(int, input().split())
graph = {i + 1 : [] for i in range(v)}

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, v + 1):
    if not d[i]:
        dfs(i, True)

cnt = 0
for i in range(1, v + 1):
    if C[i]:
        cnt += 1

print(cnt)
for i in range(1, v + 1):
    if C[i]:
        print(i, end=" ")
