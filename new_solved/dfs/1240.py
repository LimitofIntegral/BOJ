import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(start, end):
    if visited[start]:
        return 0
    visited[start] = True

    stack = tree[start]
    result = 0

    for i in stack:
        to, w = i
        if to == end:
            result += w
            break
            
        temp = dfs(to, end)

        if temp:
            result += temp + w
            break
            
    return result
    

n, m = map(int, input().split())

tree = {i + 1 : [] for i in range(n)}

for _ in range(n - 1):
    a, b, w = map(int, input().split())
    tree[a].append((b, w))
    tree[b].append((a, w))

for _ in range(m):
    visited = [False] * (n + 1)
    a, b = map(int, input().split())
    print(dfs(a, b))