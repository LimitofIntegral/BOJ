import sys


import sys
import copy
sys.setrecursionlimit(10**6)

dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

def dfs1(i, j):
    p = arr1[i][j]
    arr1[i][j] = ""
    
    for k in range(4):
        y = i + dy[k]
        x = j + dx[k]

        if y in (-1, n) or x in (-1, n):
            continue

        if arr1[y][x] == p:
            dfs1(y, x)

    return

def dfs2(i, j):
    p = arr2[i][j]
    arr2[i][j] = ""
    
    for k in range(4):
        y = i + dy[k]
        x = j + dx[k]

        if y in (-1, n) or x in (-1, n):
            continue

        if p in ("R", "G"):
            if arr2[y][x] in ("R", "G"):
                dfs2(y, x)
        else:
            if arr2[y][x] == p:
                dfs2(y, x)

    return

n = int(input())

arr1 = [list(input()) for _ in range(n)]
arr2 = [i[:] for i in arr1]
r1, r2 = 0, 0

for i in range(n):
    for j in range(n):
        if arr1[i][j]:
            dfs1(i, j)
            r1 += 1
        if arr2[i][j]:
            dfs2(i, j)
            r2 += 1

print(r1, r2)