import sys
input = sys.stdin.readline

result = float('inf')
start, end = 0, 0

n, s = map(int, input().split())
arr = list(map(int, input().split()))
temp = arr[0]

while start <= n - 1:
    if temp >= s:
        result = min(result, end - start + 1)
        temp -= arr[start]
        start += 1
    else:
        if end != n - 1:
            end += 1
            temp += arr[end]
        else:
            temp -= arr[start]
            start += 1

print(result if result != float('inf') else 0)