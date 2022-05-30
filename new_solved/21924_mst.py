import sys
import heapq as h
input = sys.stdin.readline

def prim(start):
    result = 0
    visited[start] = 0
    task = graph[start]
    h.heapify(task)
    mst = 1

    while task:
        w, to = h.heappop(task)
        if visited[to]:
            visited[to] = 0
            result += w
            mst += 1
            for i in graph[to]:
                if visited[i[1]]:
                    h.heappush(task, i)
    
    return mst, result


n, m = map(int, input().split())
graph = {i + 1 : [] for i in range(n)}
visited = [1] * (n + 1)
total = 0

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((w, b))
    graph[b].append((w, a))
    total += w

mst, result = prim(1)

print(total - result if mst == n else -1)