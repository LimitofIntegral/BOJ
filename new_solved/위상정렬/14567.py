from collections import deque

q = deque()
n, m = map(int, input().split())
graph = {i + 1 : [[], []] for i in range(n)}
t = [1] * (n + 1)
indegree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][0].append(b)
    graph[b][1].append(a)
    indegree[b] += 1

s = []
for i in range(1, n + 1):
    if not indegree[i]:
        q.append(i)

while q:
    task = q.popleft()
    s.append(task)
    for i in graph[task][0]:
        indegree[i] -= 1
        if not indegree[i]:
            q.append(i)

for i in s:
    if graph[i][1]:
        t[i] = 1 + max([t[j] for j in graph[i][1]])

print(*t[1:])