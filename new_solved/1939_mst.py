import sys
import heapq as h
input = sys.stdin.readline

def prim(start):
    result = float('inf')
    visited[start] = 0
    task = graph[start]
    h.heapify(task)

    while task:
        w, to = h.heappop(task)
        if visited[to]:
            visited[to] = 0
            if -w < result:
                result = -w
            if to == e:
                return result
            for i in graph[to]:
                if visited[i[1]]:
                    h.heappush(task, i)
    
    return result


n, m = map(int, input().split())
graph = {i + 1 : [] for i in range(n)}
visited = [1] * (n + 1)

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((-w, b))
    graph[b].append((-w, a))

s, e = map(int, input().split())
print(prim(s))
