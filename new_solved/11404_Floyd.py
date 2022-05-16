import sys
input = sys.stdin.readline
inf = float('inf')

n = int(input())
graph = [[inf] * n for _ in range(n)]

for _ in range(int(input())):
    a, b, w = map(int, input().split())
    graph[a - 1][b - 1] = min(graph[a - 1][b - 1], w)

for i in range(n):
    graph[i][i] = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

for i in range(n):
    for j in range(n):
        if j == 0:
            print(graph[i][j] if graph[i][j] != inf else 0, end = "")
        else:
            print(" ", end="")
            print(graph[i][j] if graph[i][j] != inf else 0, end = "")
    if i != n - 1:
        print()