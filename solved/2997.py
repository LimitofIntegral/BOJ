arr = list(map(int, input().split()))

arr.sort()

d1 = arr[1] - arr[0]
d2 = arr[2] - arr[1]

if d2 == d1:
    print(arr[2] + d1)
else:
    if d1 * 2 == d2:
        print(arr[1] + d1)
    else:
        print(arr[0] + d2)