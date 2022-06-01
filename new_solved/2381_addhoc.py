import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

M, m = -float('inf'), float('inf')

for i in range(n):
    M = max(M, arr[i][0] + arr[i][1])
    m = min(m, arr[i][0] + arr[i][1])

result = M - m
M, m = - float('inf'), float('inf')
for i in range(n):
    M = max(M, arr[i][0] - arr[i][1])
    m = min(m, arr[i][0] - arr[i][1])

print(max(result, M - m))