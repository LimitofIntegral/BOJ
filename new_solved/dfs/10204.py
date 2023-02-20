import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(now, step=1):
    visited[int(now[1:])] = step
    if step == 3:
        return
    
    for to in G[now]:
        if not visited[int(to[1:])]:
            dfs(to, step + 1)
        else:
            if step + 1 < visited[int(to[1:])]:
                dfs(to, step + 1)

for _ in range(int(input())):
    n, e, *a = input().split()
    n, e = int(n), int(e)
    G = {"v" + str(i) : [] for i in range(1, n + 1)}
    start = a.pop()
    visited = [0] * (n + 1)

    for i in range(e):
        G[a[i * 2]].append(a[i * 2 + 1])
        G[a[i * 2 + 1]].append(a[i * 2])
    
    dfs(start)
    
    res = sum([1 for i in visited if i])

    print(f'The number of supervillains in 2-hop neighborhood of {start} is {res - 1}')
