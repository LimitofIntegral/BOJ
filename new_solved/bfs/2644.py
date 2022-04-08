from collections import deque

def bfs(start, end):
    visited = []
    count = 0
    q = deque([start])

    while q:
        count += 1
        for _ in range(len(q)):
            n = q.popleft()
            if n == end:
                return True, count - 1
            if n not in visited:
                visited.append(n)
                q.extend(graph[n])
    
    return False, -1


n = int(input())
graph = {i + 1 : [] for i in range(n)}
x, y = map(int, input().split())
for _ in range(int(input())):
    p, c = map(int, input().split())
    graph[p].append(c)
    graph[c].append(p)

result = bfs(x, y)

if result[0]:
    print(result[1])
else:
    print(result[1])