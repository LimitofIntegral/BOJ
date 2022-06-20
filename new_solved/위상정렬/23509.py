import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n = int(input())
graph = defaultdict(list)
ind = defaultdict(int)

for _ in range(n):
    a, b = input().split()
    graph[a].append(b)
    ind[b] += 1

q = deque([i for i in graph if not ind[i]])

s = []
while q:
    temp = []
    for _ in range(len(q)):
        now = q.popleft()
        temp.append(now)

        for i in graph[now]:
            ind[i] -= 1
            if not ind[i]:
                q.append(i)
    s += sorted(temp)

if len(s) == len(graph):
    for i in s:
        print(i)
else:
    print(-1)
