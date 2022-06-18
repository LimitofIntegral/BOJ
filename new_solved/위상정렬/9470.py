import sys
from collections import deque
input = sys.stdin.readline

q = deque()

for _ in range(int(input())):
    k, m, p = map(int, input().split())
    gin = [[] for _ in range(m + 1)]
    gout = [[] for _ in range(m + 1)]
    ind = [0] * (m + 1)
    result = [1] * (m + 1)

    for _ in range(p):
        a, b = map(int, input().split())
        gin[b].append(a)
        gout[a].append(b)
        ind[b] += 1
    
    for i in range(1, m + 1):
        if not ind[i]:
            q.append(i)
    
    s = []
    while q:
        t = q.popleft()
        s.append(t)
        for i in gout[t]:
            ind[i] -= 1
            if not ind[i]:
                q.append(i)
    
    for i in s:
        if not gin[i]:
            continue

        if len(gin[i]) == 1:
            result[i] = result[gin[i][0]]
            continue
        
        arr = sorted([result[j] for j in gin[i]], reverse=True)

        if arr[0] == arr[1]:
            result[i] = arr[0] + 1
        else:
            result[i] = arr[0]
    
    print(k, result[s[-1]])
        