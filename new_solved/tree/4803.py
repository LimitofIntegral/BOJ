import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(n, before=0):
    v.add(n)

    for i in graph[n]:
        if i == before:
            continue

        if i in v:
            return 0
        else:
            if not dfs(i, n):
                return 0
    
    return 1


n, m = map(int, input().split())
case = 1
while n or m:
    graph = {i + 1 : [] for i in range(n)}
    v = set()

    for _ in range(m):
        a, b = map(int, input().split())
        if a == b:
            v.add(a)
            continue
        graph[a].append(b)
        graph[b].append(a)
    
    res = 0
    for i in graph:
        if i not in v:
            res += dfs(i)

    if res:
        print("Case %d: There is one tree." % case if res == 1 else "Case %d: A forest of %d trees." % (case, res))
    else:
        print("Case %d: No trees." % case)
    case += 1

    n, m = map(int, input().split())