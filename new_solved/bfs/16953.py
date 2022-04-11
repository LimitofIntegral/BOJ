from collections import deque

result = 0
find = False
a, b = map(int, input().split())
q = deque([a])

while q:
    result += 1
    for _ in range(len(q)):
        t = q.popleft()
        if t * 2 == b:
            find = True
            break
        elif t * 2 < b:
            q.append(t * 2)

        if t * 10 + 1 == b:
            find = True
            break
        elif t * 10 + 1 < b:
            q.append(t * 10 + 1)
    if find:
        break

if find:
    print(result + 1)
else:
    print(-1)