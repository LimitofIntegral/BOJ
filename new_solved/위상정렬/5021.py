from collections import deque, defaultdict

def init():
    return [0, [], []]

n, m = map(int, input().split())
q = deque()
graph = defaultdict(init)
root = input()
graph[root][0] = 1
indegree = {root : 0}

for _ in range(n):
    a, b, c = input().split()
    graph[a][1].append(b)
    graph[a][1].append(c)
    graph[b][2].append(a)
    graph[c][2].append(a)
    indegree[a] = 2

for i in graph:
    if not graph[i][1]:
        indegree[i] = 0

for i in indegree:
    if not indegree[i]:
        q.append(i)

s = []
while q:
    h = q.popleft()
    s.append(h)
    for i in graph[h][2]:
        indegree[i] -= 1
        if not indegree[i]:
            q.append(i)

for i in s:
    if graph[i][1]:
        for j in graph[i][1]:
            graph[i][0] += graph[j][0] * 0.5

result = []

for _ in range(m):
    t = input()
    result.append((graph[t][0], t))

result.sort(reverse=True)
print(result[0][1])
