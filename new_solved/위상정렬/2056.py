from collections import deque

q = deque([])
result = 0
n = int(input())
graph = {i + 1 : [0, [], []] for i in range(n)}
indegree = [0] * (n + 1)
t = [0] * (n + 1)

for i in range(1, n + 1):
    c = input().split()

    if len(c) == 2:
        graph[i][0] = int(c[0])
        t[i] = int(c[0])
    else:
        graph[i][0] = int(c[0])
        indegree[i] = int(c[1])
        for j in c[2:]:
            graph[int(j)][1].append(i)
            graph[i][2].append(int(j))

s = []
for i in range(1, n + 1):
    if not indegree[i]:
        q.append(i)

while q:
    task = q.popleft()
    s.append(task)
    for i in graph[task][1]:
        indegree[i] -= 1
        if not indegree[i]:
            q.append(i)

for i in s:
    if graph[i][2]:
        t[i] = graph[i][0] + max([t[j] for j in graph[i][2]])
    result = max(result, t[i])

print(result)
