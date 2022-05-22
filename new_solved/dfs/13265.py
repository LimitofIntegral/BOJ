import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(start, color):
    global result
    visited[start] = color
    stack = sorted(graph[start][:])
    if color:
        c = 0
    else:
        c = 1
    while stack:
        to = stack.pop()
        if to in visited:
            if visited[to] != c:
                result = False
                break
        else:
            dfs(to, c)
    
    return
        

for _ in range(int(input())):
    result = True
    n, m = map(int, input().split())
    graph = {i + 1 : [] for i in range(n)}
    visited = {}
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1, n + 1):
        if i not in visited:
            dfs(i, 0)
    print("possible" if result else "impossible")