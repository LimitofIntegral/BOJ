import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

for i in range(N):
    arr[i] = [arr[i], i]

arr.sort()

for i in range(N):
    if i == 0:
        t = arr[i][0]
        arr[i][0] = 0
    else:
        p = arr[i - 1][0]
        if arr[i][0] == t:
            arr[i][0] = p
        else:
            t = arr[i][0]
            arr[i][0] = p + 1

arr.sort(key=lambda x: x[1])

for i in arr:
    print(i[0], end= " ")