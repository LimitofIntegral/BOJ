def dfs(now, step=1):
    res[now] = step

    for to in G[now]:
        if not res[to]:
            dfs(to, step + 1)


n = int(input())
G = {i + 1 : [] for i in range(n)}
res = [0] * (n + 1)

for i in range(1, n + 1):
    parent = int(input())
    if parent == -1:
        start = i
    else:
        G[i].append(parent)
        G[parent].append(i)

dfs(start)

for i in range(n):
    print(res[i + 1] - 1)