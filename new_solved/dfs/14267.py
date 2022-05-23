import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(start, w = 0):
    result[start] += w
    stack = graph[start]

    while stack:
        to = stack.pop()
        dfs(to, result[start])
    
    return


n, m = map(int, input().split())
graph = {i + 1 : [] for i in range(n)}
result = [0] * (n + 1)
for idx, i in enumerate(list(map(int, input().split()))):
    if idx == 0:
        continue
    graph[i].append(idx + 1)

for _ in range(m):
    a, b = map(int, input().split())
    result[a] = b

dfs(1)

print(*result[1:])
