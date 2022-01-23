N, K = map(int, input().split())

arr = [i for i in range(1, N + 1)]

j = 0

print("<", end = "")

while len(arr) != 1:
    j += K - 1
    if j > N - 1:
        j %= N
    print(arr[j], end = ", ")
    del arr[j]
    N -= 1

print(str(arr[0]) + ">")