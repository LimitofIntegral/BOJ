n, m = map(int, input().split())
r = 1
arr = []

for _ in range(n):
    arr.append(list(input()))

if n > m:
    temp = []
    for i in range(m):
        line = []
        for j in range(n):
            line.append(arr[j][i])
        temp.append(line)
    arr = temp

print(arr)