# 생각해보니 dfs 재귀로 짜겠다고 graph 인자로 줘놓고 재귀를 안씀 ㅋㅋ

def dfs(graph, start):
    visited, stack = [start], [start]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)

        for i in graph[n]:
            if i not in visited:
                visited.append(i)
                stack.extend(graph[i])
    return visited

for _ in range(int(input())):
    a = list(map(int, input().split()))
    graph = {i : [] for i in range(a[0])}
    for i in range(a[1]):
        n1, n2 = a[2 + 2 * i], a[3 + 2 * i]
        graph[n1].append(n2)
        graph[n2].append(n1)
    result = dfs(graph, 0)
    
    if len(dfs(graph, 0)) == a[0]:
        print("Connected.")
    else:
        print("Not connected.")