arr = list(map(int, input().split()))

arr.sort()

d = {'A' : arr[0], 'B' : arr[1], 'C' : arr[2]}

cmd = list(input())

for i in cmd:
    print(d[i], end = ' ')