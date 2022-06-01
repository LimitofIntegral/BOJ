import sys
import heapq as h
input = sys.stdin.readline

def prim(start):
    result = 0
    visited[start] = 0
    task = graph[start]
    h.heapify(task)

    while task:
        w, to = h.heappop(task)
        if visited[to]:
            visited[to] = 0
            result += w
            for i in graph[to]:
                if visited[i[1]]:
                    h.heappush(task, i)

    return result


for _ in range(int(input())):
    r, c = map(int, input().split())
    graph = {i + 1 : [] for i in range(r * c)}
    visited = [1] * (r * c + 1)
    arr = [[(j * c) + i + 1 for i in range(c)] for j in range(r)]

    for i in range(r):
        temp = list(map(int, input().split()))
        for j in range(c - 1):
            graph[arr[i][j]].append((temp[j], arr[i][j + 1]))
            graph[arr[i][j + 1]].append((temp[j], arr[i][j]))

    for i in range(r - 1):
        temp = list(map(int, input().split()))
        for j in range(c):
            graph[arr[i][j]].append((temp[j], arr[i + 1][j]))
            graph[arr[i + 1][j]].append((temp[j], arr[i][j]))
    
    print(prim(1))
