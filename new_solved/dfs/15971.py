import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(start, w = 0):
    global result
    if result:
        return
    visited[start] = w
    if start == e:
        temp = [visited[i] for i in visited]
        result = sum(temp) - max(temp)
        return
    stack = sorted(graph[start][:])

    while stack:
        to, w_ = stack.pop()
        if to not in visited:
            dfs(to, w_)
    
    visited.pop(start)
    return


n, s, e = map(int, input().split())
graph = {i + 1 : [] for i in range(n)}
visited, result = {}, 0

for _ in range(n - 1):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

dfs(s)
print(result)