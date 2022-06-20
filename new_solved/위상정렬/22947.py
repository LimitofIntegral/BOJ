import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

n, m, k = map(int, input().split())
t = [0] + list(map(int, input().split()))
graph = {i + 1 : [[], []] for i in range(n)}
ind = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][0].append(b)
    graph[b][1].append(a)
    ind[b] += 1

q = deque([1])
s = []
while q:
    now = q.popleft()
    s.append(now)
    for i in graph[now][0]:
        ind[i] -= 1
        if not ind[i]:
            q.append(i)

end = s[-1]

arr = list(combinations(s[1:-1], k))

result = float('inf')

for i in range(len(arr)):
    t_ = t[:]

    for j in arr[i]:
        t_[j] = 0
    
    for j in s:
        if graph[j][1]:
            w = 0
            for k in graph[j][1]:
                w = max(w, t_[k] + t_[j])
            t_[j] = max(t_[j], w)
    
    result = min(result, t_[end])

print(result)
