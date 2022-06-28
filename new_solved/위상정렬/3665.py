import sys
from collections import deque
input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())

    if not m:
        print(*a)
        continue

    graph = {i + 1 : {} for i in range(n)}
    ind = [0] * (n + 1)

    for i in range(n - 1):
        for j in range(i + 1, n):
            graph[a[i]][a[j]] = None
            ind[a[j]] += 1

    for _ in range(m):
        x, y = map(int, input().split())

        if y in graph[x]:
            del graph[x][y]
            graph[y][x] = None
            ind[y] -= 1
            ind[x] += 1
        else:
            del graph[y][x]
            graph[x][y] = None
            ind[x] -= 1
            ind[y] += 1
    
    q = deque([i for i in range(1, n + 1) if not ind[i]])

    s, check = [], False

    while q:
        now = q.popleft()
        s.append(now)

        if q:
            print("IMPOSSIBLE")
            check = True
            break

        for i in graph[now]:
            if not ind[i]:
                print("?")
                check = True
                break
            ind[i] -= 1
            if not ind[i]:
                q.append(i)
        
        if check:
            break
    
    if not check and len(s) == n:
        print(*s)
    else:
        print("IMPOSSIBLE")
