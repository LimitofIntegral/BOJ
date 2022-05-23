import heapq as h
import sys
input = sys.stdin.readline

def d(start, end):
    dist = [float('inf')] * (n + 1)
    task = [(0, start)]
    dist[start] = 0
    while task:
        w, to = h.heappop(task)
        if dist[to] < w:
            continue
        for w_, to_ in graph[to]:
            if dist[to_] > dist[to] + w_:
                dist[to_] = dist[to] + w_
                h.heappush(task, (dist[to_], to_))
    return dist[end]


inf = float('inf')

n, m, x = map(int, input().split())
graph = {i + 1 : [] for i in range(n)}

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((w, b))

result = 0

for i in range(1, n + 1):
    if i == x:
        continue
    result = max(result, d(i, x) + d(x, i))

print(result)