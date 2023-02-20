import sys
input = sys.stdin.readline

n, l = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(n)]

arr.sort()

total = [list(arr[0])]

for i in range(1, n):
    if arr[i][0] <= total[-1][1]:
        total[-1][1] = arr[i][1]
    else:
        total.append(list(arr[i]))

print(total)