from collections import deque
import sys

input = sys.stdin.readline

def bfs():
    q = deque([1])
    while q:
        p = q.popleft()
        for i in graph[p]:
            if i not in visited:
                visited[i] = p
                q.append(i)


visited = {}
n = int(input())

graph = {i + 1 : [] for i in range(n)}

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs()

for i in range(2, n + 1):
    print(visited[i])