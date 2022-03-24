def dfs(graph, n):
    stack, visit = [], [n]
    try:
        stack.extend(graph[n])
    except:
        pass

    while stack:
        node = stack.pop()
        if node not in visit:
            stack.extend(graph[node])
            visit.append(node)
    
    return visit

graph = {}

n = int(input())
for _ in range(int(input())):
    a, b = map(int, input().split())
    try:
        graph[a] += [b]
    except:
        graph[a] = [b]
    try:
        graph[b] += [a]
    except:
        graph[b] = [a]

print(len(dfs(graph, 1)) - 1)