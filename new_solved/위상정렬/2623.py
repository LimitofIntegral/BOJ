import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    a = list(map(int, input().split()))
    for i in range(1, a[0]):
        for j in range(i + 1, a[0] + 1):
            graph[a[i]].append(a[j])
            indegree[a[j]] += 1

q = deque()
for i in range(1, n + 1):
    if not indegree[i]:
        q.append(i)

s = []
while q:
    i = q.popleft()
    s.append(i)
    for j in graph[i]:
        indegree[j] -= 1
        if not indegree[j]:
            q.append(j)

if len(s) == n:
    for i in s:
        print(i)
else:
    print(0)
