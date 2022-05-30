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

n = int(input())
graph = {i : [] for i in range(n)}
visited = [1] * n
total = 0

for i in range(n):
    temp = list(input().strip())
    for j in range(n):
        p = ord(temp[j])
        if p == 48:
            pass
        else:
            if p < 97:
                w = p - 38
            else:
                w = p - 96
            total += w
            graph[i].append((w, j))
            graph[j].append((w, i))

mst, result = prim(0)

print(total - result if mst == n else -1)
