import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

def dfs(start, w = 0, visited = {}):
    global temp, node
    visited[start] = None
    stack = graph[start][:]

    while stack:
        w_, to = stack.pop()
        if to not in visited:
            dfs(to, w + w_, visited)

    if temp < w:
        temp, node = w, start

    visited.pop(start)
    return


graph = defaultdict(list)
temp, node = 0, 0

while True:
    try:
        a, b, w = map(int, input().split())
        graph[a].append((w, b))
        graph[b].append((w, a))
    except:
        break

if graph:
    dfs(1)
    dfs(node)
    print(temp)
else:
    print(0)
