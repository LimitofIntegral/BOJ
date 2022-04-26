from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    depth = 0
    q = deque([start])
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if node not in visited:
                visited[node] = depth
                # 까먹고 안뺐는데 트리 깊이만 관련돼서 reverse가 상관 X
                graph[node].sort(key = int, reverse = True)
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

for i in range(n):
    p = str(i + 1)
    if p in visited:
        print(visited[p])
    else:
        print(-1)
