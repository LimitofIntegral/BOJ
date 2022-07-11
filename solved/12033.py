from collections import deque

q = deque()
for i in range(int(input())):
    print(f"Case #{i + 1}:", end= " ")
    n = int(input())
    t = list(map(int, input().split()))
    for j in t:
        if q:
            if j * 3 // 4 == q[0]:
                print(q.popleft(), end = " ")
            else:
                q.append(j)
        else:
            q.append(j)
    print()