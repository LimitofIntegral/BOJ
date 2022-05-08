import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(start, stack):
    global step
    node = start
    stack.extend(sorted(graph[node], reverse=True))

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited[node] = None
        result[node] = step
        step += 1
        dfs(node, stack)
    
    return


n, m, r = map(int, input().split())
visited, step = {r : None}, 2
result = [0] * (n + 1)
result[r] = 1
graph = {i + 1 : [] for i in range(n)}

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(r, [])

for i in range(1, n + 1):
    print(result[i])