from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    visited = {start : None}
    q = deque(graph[start])
    step = 0

    while q:
        step += 1
        for _ in range(len(q)):
            node = q.popleft()
            if node in visited:
                continue
            visited[node] = None
            result[start - 1] += step
            q.extend(graph[node])
    return


n, m = map(int, input().split())
graph = { i + 1 : [] for i in range(n) }
result = [0] * (n)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    bfs(i)

temp = min(result)

for i in range(n):
    if result[i] == temp:
        print(i + 1)
        break