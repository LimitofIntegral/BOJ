import sys
from collections import deque
input = sys.stdin.readline

dx = (0, -1, 0, 1)
dy = (-1, 0, 1, 0)
inf = 2 ** 31 - 1

def bfs():
    i, j = n - 1, n - 1
    q = deque([(i, j)])
    task = {(i, j) : 1}

    while q:
        for _ in range(len(q)):
            i, j = q.popleft()
            p = task.pop((i, j))

            for k in range(2):
                y = i + dy[k]
                x = j + dx[k]

                if y < 0 or x < 0 or arr[y][x] == -1:
                    continue

                arr[y][x] += p
                arr[y][x] %= inf

                if (y, x) in task:
                    task[(y, x)] += p
                    task[(y, x)] %= inf
                else:
                    task[(y, x)] = arr[y][x]
        q = deque([i for i in task])


def check():
    q, visited = deque([(0, 0)]), {}

    while q:
        i, j = q.popleft()

        for k in range(4):
            y = i + dy[k]
            x = j + dx[k]

            if (y, x) == (n - 1, n - 1):
                return True

            if y in (-1, n) or x in (-1, n) or arr[y][x] == -1:
                continue

            if (y, x) not in visited:
                q.append((y, x))
                visited[y, x] = None
    
    return False


n = int(input())
arr = [[0 if i == "." else -1 for i in list(input().strip())] for _ in range(n)]
bfs()

if arr[0][0]:
    print(arr[0][0])
else:
    print("THE GAME IS A LIE" if check() else "INCONCEIVABLE")
