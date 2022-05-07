import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(start, visited, temp):
    global result
    stack = sorted(graph[start], reverse=True)
    while stack:
        to, w = stack.pop()
        if to in visited:
            continue
        visited[to] = None
        dfs(to, visited, temp + w)
    
    result = max(result, temp)
    return


n = int(input())
graph = {i + 1 : [] for i in range(n)}

for _ in range(n - 1):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

result = 0

dfs(1, {1:None}, 0)
print(result)