def dfs(start):
    visited, stack = [], [start]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack.extend(graph[n])
    
    return visited

n, m = map(int, input().split())
graph = {i : [] for i in range(n)}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

result = dfs(0)

if n == len(result):
    print(0)
else:
    for i in range(n):
        if i not in result:
            print(i + 1)