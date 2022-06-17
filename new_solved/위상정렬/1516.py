from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = {i + 1 : [[], []] for i in range(n)}
indegree = [0] * (n + 1)
t = [0] * (n + 1)

for i in range(1, n + 1):
    a = list(map(int, input().split()))
    t[i] = a[0]
    if len(a) != 2:
        indegree[i] = len(a) - 2
        graph[i][1] = a[1:-1]
        for j in a[1:-1]:
            graph[j][0].append(i)

q = deque()

for i in range(1, n + 1):
    if not indegree[i]:
        q.append(i)

s = []

while q:
    to = q.popleft()
    s.append(to)
    for i in graph[to][0]:
        indegree[i] -= 1
        if not indegree[i]:
            q.append(i)

for i in s:
    if graph[i][1]:
        w = 0
        for j in graph[i][1]:
            w = max(w, t[j])
        t[i] += w

for i in range(1, n + 1):
    print(t[i])