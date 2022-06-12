import sys
sys.setrecursionlimit(2*10**5)
input = sys.stdin.readline

def dfs(start, before=-1, color=0):
    global result
    task = graph[start]
    c = arr[start]

    if color != c:
        result += 1
        for i in task:
            if i != before:
                dfs(i, start, c)
    else:
        for i in task:
            if i != before:
                dfs(i, start, color)
                

n = int(input())
arr = [0] + list(map(int, input().split()))
graph = {i + 1 : [] for i in range(n)}
result = 0

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
print(result)