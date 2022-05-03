import heapq as h
import sys
input = sys.stdin.readline

visited = {}
heap = []

n, m = map(int, input().split())
start = int(input())

graph = {i + 1 : {} for i in range(n)}

for _ in range(m):
    a, b, w = map(int, input().split())
    try:
        graph[a][b] = min(w, graph[a][b])
    except:
        graph[a][b] = w


d = [float('inf')] * (n + 1)
d[start] = 0

for i in graph[start]:
    d[i] = min(d[i], graph[start][i])
    h.heappush(heap, (graph[start][i], i))


while heap:
    w, node = h.heappop(heap)
    if node in visited:
        continue
    visited[node] = None
    for i in graph[node]:
        d[i] = min(d[i], w + graph[node][i])
        h.heappush(heap, (d[i], i))

for i in range(1, n + 1):
    print("INF" if d[i] == float('inf') else d[i])