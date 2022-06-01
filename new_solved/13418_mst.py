import sys
import heapq as h
input = sys.stdin.readline

def prim():
    rm, rM = 0, 0
    visited = [1] * (n + 1)
    visited[0] = 0

    task = graph[0][0]
    h.heapify(task)

    while task:
        w, to = h.heappop(task)
        if visited[to]:
            visited[to] = 0
            if not w:
                rm += 1
            for i in graph[0][to]:
                if visited[i[1]]:
                    h.heappush(task, i)
        
    visited = [1] * (n + 1)
    visited[0] = 0

    task = graph[1][0]
    h.heapify(task)

    while task:
        w, to = h.heappop(task)
        if visited[to]:
            visited[to] = 0
            if not w:
                rM += 1
            for i in graph[1][to]:
                if visited[i[1]]:
                    h.heappush(task, i)
        
    if rm:
        rm *= rm
    if rM:
        rM *= rM

    return rm - rM


n, m = map(int, input().split())
graph = [{i : [] for i in range(n + 1)} for _ in range(2)]
for _ in range(m + 1):
    a, b, w = map(int, input().split())

    graph[0][a].append((w, b))
    graph[0][b].append((w, a))
    graph[1][a].append((-w, b))
    graph[1][b].append((-w, a))

print(prim())