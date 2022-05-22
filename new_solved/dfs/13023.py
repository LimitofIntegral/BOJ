import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(start, step):
    global result

    if step == 5:
        result = True
        return

    visited[start] = None
    stack = sorted(graph[start][:])

    while stack:
        to = stack.pop()
        if to not in visited:
            dfs(to, step + 1)
    
    visited.pop(start)
    return

n, m = map(int, input().split())
graph = {i : [] for i in range(n)}
result = False

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    visited = {}
    dfs(i, 1)
    if result:
        break

print(1 if result else 0)