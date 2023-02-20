import sys
input = sys.stdin.readline


n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]

arr.sort()

line = [list(arr[0])]

for i in range(1, n):
    if arr[i][0] <= line[-1][1]:
        line[-1][1] = max(line[-1][1], arr[i][1])
    else:
        line.append(list(arr[i]))

d = 0

for i in line:
    d += i[1] - i[0]

print(d)