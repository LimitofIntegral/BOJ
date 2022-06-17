import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = {i + 1 : [] for i in range(n)}
indegree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    indegree[b] += 1
    graph[a].append(b)

q = deque()

for i in range(1, n + 1):
    if not indegree[i]:
        q.append(i)

s = []

while q:
    t = q.popleft()
    s.append(t)
    for i in graph[t]:
        indegree[i] -= 1
        if not indegree[i]:
            q.append(i)

print(*s)