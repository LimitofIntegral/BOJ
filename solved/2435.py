n, k = map(int, input().split())
arr = list(map(int, input().split()))
result = -10001

for i in range(n - k + 1):
    t = 0
    for j in range(k):
        t += arr[i + j]
    result = max(result, t)

print(result)