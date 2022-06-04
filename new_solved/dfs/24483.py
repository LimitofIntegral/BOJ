import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(s, depth=0):
    global step, result
    visited[s] = 0
    result += step * depth
    step += 1

    task = sorted(graph[s][:], reverse=True)

    while task:
        to = task.pop()
        if visited[to]:
            dfs(to, depth + 1)
    
    return


n, m, r = map(int, input().split())
graph = {i + 1 : [] for i in range(n)}
visited = [1] * (n + 1)
step = 1
result = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(r)
print(result)