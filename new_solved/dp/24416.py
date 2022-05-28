n = int(input())

arr = [0] * 40
arr[0], arr[1] = 1, 1

for i in range(2, 40):
    arr[i] = arr[i - 1] + arr[i - 2]

print(arr[n - 1], n - 2)