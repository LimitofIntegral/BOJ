import sys
sys.setrecursionlimit(10 ** 4)
# 어디서 재귀가 터지는진 모르겠는데 추가하니까 통과

def search(i, j):
    global count
    if (i, j) not in visited:
        visited.append((i, j))
        if field[i][j]:
            count += 1
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if x < 0 or x >= n or y < 0 or y >= m:
                    continue
                search(x, y)
    else:
        return

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

for _ in range(int(input())):
    visited = []
    cnt = []
    n, m, k = map(int, input().split())
    field = [[0] * m for _ in range(n)]
    for _ in range(k):
        i, j = map(int, input().split())
        field[i][j] = 1
    for i in range(n):
        for j in range(m):
            count = 0
            search(i, j)
            if count:
                cnt.append(count)
    print(len(cnt))
