import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(start, level):
    stack = sorted(graph[start], reverse=True)

    while stack:
        node = stack.pop()
        if visited[node] == -1:
            visited[node] = level
            dfs(node, level + 1)
    
    return

n, m, r = map(int, input().split())
graph = {i + 1 : [] for i in range(n)}
visited = [-1] * (n + 1)
visited[r] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(r, 1)

for i in range(1, n + 1):
    print(visited[i])