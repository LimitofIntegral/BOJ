import sys
import heapq as h
input = sys.stdin.readline

def prim(start):
    total = 0
    visited[start] = 0
    task = graph[start]
    h.heapify(task)
    
    while task:
        w, to = h.heappop(task)
        if visited[to]:
            visited[to] = 0
            total += w
            for i in graph[to]:
                h.heappush(task, i)
    
    return total


n = int(input())

graph = {i : [] for i in range(n)}
visited = [1] * n

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(i + 1, n):
        graph[i].append((temp[j], j))
        graph[j].append((temp[j], i))

print(prim(0))
