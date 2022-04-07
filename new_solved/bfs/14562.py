from collections import deque

def bfs(s, t):
    count = 0
    q = deque([(s, t)])
    while True:
        count += 1
        for _ in range(len(q)):
            a, b = q.popleft()
            if a * 2 == b + 3:
                return count
            if a * 2 < b + 3:
                q.append((a * 2, b + 3))
            
            if a + 1 == b:
                return count
            else:
                q.append((a + 1, b))


for _ in range(int(input())):
    s, t = map(int, input().split())
    print(bfs(s, t))
