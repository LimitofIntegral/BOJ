arr = [1]
i = 2
while len(arr) < 1000:
    temp = [i] * i
    arr += temp
    i += 1

a, b = map(int, input().split())

print(sum(arr[a - 1:b]))