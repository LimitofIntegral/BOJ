import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(n):
    w, v = map(int, input().split())
    for j in range(m + 1):
        if j - w >= 0:
            arr[i + 1][j] = max(arr[i][j], v + arr[i][j - w])
        else:
            arr[i + 1][j] = arr[i][j]

print(arr[-1][-1])
for i in arr:
    print(i)