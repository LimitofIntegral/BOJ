import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def set_depth(root, d = 0):
    depth[root] = d
    for i in graph[root]:
        if i != parent[root]:
            set_depth(i, d + 1)
    return


def lca(a, b):
    if depth[a] > depth[b]:
        a, b = b, a
    
    while depth[a] != depth[b]:
        b = parent[b]
        if a == b:
            return a
    
    while parent[a] != parent[b]:
        a, b = parent[a], parent[b]
    
    return parent[a]


for _ in range(int(input())):
    n = int(input())
    parent, depth = [0] * (n + 1), [0] * (n + 1)
    graph = {i + 1 : [] for i in range(n)}

    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        parent[b] = a

    for i in range(1, n + 1):
        if parent[i] == 0:
            root = i
            break

    set_depth(root)

    a, b = map(int, input().split())
    print(lca(a, b))