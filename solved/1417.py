n = int(input())

arr = []
count = 0

for i in range(n):
    arr.append(int(input()))

d = arr[0]
arr = arr[1:]

if n == 1:
    print(0)
else:
    while d <= max(arr):
        d += 1
        arr[arr.index(max(arr))] -= 1
        count += 1
    print(count)