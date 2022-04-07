result = 0
visited = []

n, m = map(int, input().split())
graph = [[0] * n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1

for i in range(n):
    stack = []
    if i in visited:
        continue
    result += 1
    visited.append(i)
    temp = graph[i]
    for j in range(n):
        if temp[j]:
            stack.append(j)
    while stack:
        p = stack.pop()
        if p in visited:
            continue
        visited.append(p)
        temp = graph[p]
        for j in range(n):
            if temp[j]:
                stack.append(j)

print(result)