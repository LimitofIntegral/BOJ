def bfs(graph, start):
    visit, queue = [], [start]

    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            try:
                queue.extend(sorted(graph[node]))
            except:
                pass
    
    return visit


def dfs(graph, start):
    visit, stack = [], [start]

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            try:
                stack.extend(sorted(graph[node], reverse=True))
            except:
                pass
    return visit


n, m, s = map(int, input().split())

graph = {}

for i in range(m):
    a, b = map(int, input().split())
    try: 
        graph[a].append(b)
    except:
        graph[a] = [b]
    
    try:
        graph[b].append(a)
    except:
        graph[b] = [a]

for i in dfs(graph, s):
    print(i, end = " ")
print()
for i in bfs(graph, s):
    print(i, end = " ")