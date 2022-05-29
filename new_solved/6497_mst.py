import sys
import heapq as h
input = sys.stdin.readline

def prim(start):
    result = 0
    visited[start] = 0
    task = graph[start]
    h.heapify(task)
    mst = [start]

    while task:
        w, to = h.heappop(task)
        if visited[to]:
            visited[to] = 0
            mst.append(to)
            result += w
            for i in graph[to]:
                if visited[i[1]]:
                    h.heappush(task, i)
    
    return result
    

n, m = map(int, input().split())
while n and m:
    graph = {i : [] for i in range(n)}
    visited = [1] * n
    total = 0

    start = None

    for _ in range(m):
        a, b, w = map(int, input().split())
        if not start:
            start = a
        graph[a].append((w, b))
        graph[b].append((w, a))
        total += w

    print(total - prim(start))
    n, m = map(int, input().split())
