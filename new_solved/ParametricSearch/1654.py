import sys
input = sys.stdin.readline

result = 0

k, n = map(int, input().split())
arr = []

for _ in range(k):
    arr.append(int(input()))

s, e = 0, max(arr)

while s <= e:
    total = 0
    mid = (s + e) // 2

    if mid == 0:
        mid = 1

    for i in arr:
        if i >= mid:
            total += i // mid
    
    if total >= n:
        result = mid
        s = mid + 1
    else:
        e = mid - 1

print(result)