from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    step = 1
    q = deque([start])
    while q:
        node = q.popleft()
        if node not in visited:
            visited[node] = step
            step += 1
            graph[node].sort(key = int)
            q.extend(graph[node])

# sort에 key = int를 넣어야 문자열 숫자를 크기로 인식함
# 안넣으면 순서로 인식해서 원하는대로 정렬이 안됨

visited = {}

n, m, r = map(int, input().split())

graph = {str(i + 1) : [] for i in range(n)}

for _ in range(m):
    a, b = input().split()
    graph[a].append(b)
    graph[b].append(a)

bfs(str(r))

for i in range(n):
    p = str(i + 1)
    if p in visited:
        print(visited[p])
    else:
        print(0)
