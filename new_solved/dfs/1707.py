import sys
sys.setrecursionlimit(2 * 10**5)
input = sys.stdin.readline

def dfs(start, c=0, before=0):
    global result
    if not result:
        return
    
    color[start] = c
    task = graph[start][:]

    for i in task:
        if i == before:
            continue
        if color[i]:
            if color[i] == c:
                result = False
                return
        else:
            dfs(i, c ^ 1, start)
    
    return


for _ in range(int(input())):
    result = True
    v, e = map(int, input().split())
    graph = {i + 1 : [] for i in range(v)}
    color = [None] * (v + 1)

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, v + 1):
        if not color[i]:
            dfs(i)
            if not result:
                break

    print("YES" if result else "NO")