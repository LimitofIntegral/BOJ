from collections import deque

for _ in range(int(input())):
    q = deque()
    n, k = map(int, input().split())
    t = [0] + list(map(int, input().split()))
    indegree = [0] * (n + 1)
    graph = {i + 1 : [[], []] for i in range(n)}

    for _ in range(k):
        a, b = map(int, input().split())
        graph[a][1].append(b)
        graph[b][0].append(a)
        indegree[b] += 1
    
    for i in range(1, n + 1):
        if not indegree[i]:
            q.append(i)
    
    s = []
    while q:
        node = q.popleft()
        s.append(node)
        for i in graph[node][1]:
            indegree[i] -= 1
            if not indegree[i]:
                q.append(i)
    
    for i in s:
        if graph[i][0]:
            w = 0
            for j in graph[i][0]:
                w = max(w, t[j])
            t[i] += w
    
    v = int(input())
    print(t[v])
