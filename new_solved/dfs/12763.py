import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(start, time = 0, money = 0, before = 0):
    global result

    if start == n:
        if money < result:
            result = money
        return

    task = sorted(graph[start][:], reverse=True)

    while task:
        t, m, to = task.pop()
        if to == before:
            continue

        if t + time <= T and m + money <= M:
            dfs(to, t + time, m + money, start)
    
    return


n = int(input())
graph = {i + 1 : [] for i in range(n)}
T, M = map(int, input().split())

for _ in range(int(input())):
    a, b, t, m = map(int, input().split())
    graph[a].append((t, m, b))
    graph[b].append((t, m, a))

result = float('inf')
dfs(1)
print(result if result != float('inf') else -1)