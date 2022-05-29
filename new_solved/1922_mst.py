import sys
import heapq as h
input = sys.stdin.readline

def prim(start):
    total = 0
    visited[start] = 0
    task = graph[start]
    h.heapify(task)
    mst = [start]

    while task:
        w, to = h.heappop(task)
        if visited[to]:
            visited[to] = 0
            mst.append(to)
            total += w
            for i in graph[to]:
                if visited[i[1]]:
                    h.heappush(task, i)
        
    return total


n = int(input())
graph = {i + 1 : [] for i in range(n)}
visited = [1] * (n + 1)
m = int(input())

for _ in range(m):
    a, b, w = map(int, input().split())
    if a == b:
        continue
    graph[a].append((w, b))
    graph[b].append((w, a))

print(prim(1))