import sys
import heapq as h
input = sys.stdin.readline

def prim(start, p, q):
    result = False
    visited[start] = 0
    task = graph[start]
    h.heapify(task)

    while task:
        _, to, before = h.heappop(task)
        if visited[to]:
            visited[to] = 0
            if (before, to) == (p, q) or (to, before) == (p, q):
                result = True
            for i in graph[to]:
                if visited[i[1]]:
                    h.heappush(task, i)
    
    return result
    

for _ in range(int(input())):
    n, m, p, q = map(int, input().split())
    graph = {i + 1 : [] for i in range(n)}
    visited = [1] * (n + 1)

    for _ in range(m):
        a, b, w = map(int, input().split())
        graph[a].append((w, b, a))
        graph[b].append((w, a, b))
    
    print("YES" if prim(1, p, q) else "NO")