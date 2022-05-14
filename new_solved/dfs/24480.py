import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(start):
    global step
    if result[start - 1]:
        return
    result[start - 1] = step
    step += 1
    stack = sorted(graph[start])
    while stack:
        dfs(stack.pop())


n, m, r = map(int, input().split())
graph = {i + 1 : [] for i in range(n)}
result = [0] * n
step = 1

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(r)

for i in result:
    print(i)