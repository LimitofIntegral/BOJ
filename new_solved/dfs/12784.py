import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

def dfs(start, w=float('inf'), before=0):
    task = graph[start][:]

    if len(task) == 1 and task[0][1] == before:
        return w
    else:
        temp = 0
        for i in task:
            if i[1] == before:
                continue
            temp += dfs(i[1], i[0], start)
        return min(w, temp)


for _ in range(int(input())):
    n, m = map(int, input().split())
    graph = {i + 1 : [] for i in range(n)}

    for _ in range(m):
        a, b, w = map(int, input().split())
        graph[a].append((w, b))
        graph[b].append((w, a))
    
    print(dfs(1))
