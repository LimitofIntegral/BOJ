import sys
from collections import deque
input = sys.stdin.readline

dz = (1, -1, 0, 0, 0, 0)
dy = (0, 0, 1, -1, 0, 0)
dx = (0, 0, 0, 0, 1, -1)


def bfs():
    q = deque([(sz, sy, sx)])
    step = 0

    while q:
        step += 1
        for _ in range(len(q)):
            i, j, k = q.popleft()

            for a in range(6):
                z = i + dz[a]
                y = j + dy[a]
                x = k + dx[a]

                if (z, y, x) == (ez, ey, ex):
                    return step

                if z in (-1, l) or y in (-1, r) or x in (-1, c):
                    continue
                
                if arr[z][y][x] == "#" or arr[z][y][x]:
                    continue
                
                q.append((z, y, x))
                arr[z][y][x] = step

    return 0



l, r, c = map(int, input().split())

while l:
    arr = []

    for _ in range(l):
        arr.append([[0 if i == "." else i for i in list(input().strip())] for _ in range(r)])
        _ = input()

    for i in range(l):
        for j in range(r):
            for k in range(c):
                if arr[i][j][k] == "S":
                    sz, sy, sx = i, j, k
                    arr[i][j][k] = -1
                if arr[i][j][k] == "E":
                    ez, ey, ex = i, j, k
                    arr[i][j][k] = 0

    result = bfs()
    print(f"Escaped in {result} minute(s)." if result else "Trapped!")

    l, r, c = map(int, input().split())
