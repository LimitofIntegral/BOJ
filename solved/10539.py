n = int(input())
arr = list(map(int, input().split()))

s, r = 0, 0

for i in range(n):
    r = arr[i] * (i + 1)
    print(r - s, end = " ")
    s = r