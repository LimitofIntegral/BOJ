from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    step = 1
    depth = 0
    q = deque([start])
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if node not in visited:
                visited[node] = step, depth
                step += 1
                graph[node].sort(key = int)
                q.extend(graph[node])
        depth += 1

visited = {}

n, m, r = map(int, input().split())

graph = {str(i + 1) : [] for i in range(n)}

for _ in range(m):
    a, b = input().split()
    graph[a].append(b)
    graph[b].append(a)

bfs(str(r))

result = 0

for i in range(n):
    p = str(i + 1)
    if p in visited:
        result += visited[p][0] * visited[p][1]

print(result)
