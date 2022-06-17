import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[[], []] for _ in range(n + 1)]
indegree = [0] * (n + 1)
t = [0] + [int(input()) for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][0].append(b)
    graph[b][1].append(a)
    indegree[b] += 1

q = deque()
for i in range(1, n + 1):
    if not indegree[i]:
        q.append(i)

s = []
while q:
    c = q.popleft()
    s.append(c)
    for i in graph[c][0]:
        indegree[i] -= 1
        if not indegree[i]:
            q.append(i)

result = 0

for i in s:
    if graph[i][1]:
        w = 0
        for j in graph[i][1]:
            w = max(w, t[j])
        t[i] += w
    result = max(result, t[i])

print(result)