from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    step = 1
    q = deque([start])
    while q:
        node = q.popleft()
        if node not in visited:
            visited[node] = step
            step += 1
            graph[node].sort(key = int, reverse = True)
            q.extend(graph[node])

visited = {}

n, m, r = map(int, input().split())

graph = {str(i + 1) : [] for i in range(n)}

for _ in range(m):
    a, b = input().split()
    graph[a].append(b)
    graph[b].append(a)

bfs(str(r))

for i in range(n):
    p = str(i + 1)
    if p in visited:
        print(visited[p])
    else:
        print(0)
