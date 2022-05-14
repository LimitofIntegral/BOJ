n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

result = 0

arr1.sort(reverse=True)
arr2.sort()

if n >= m:
    for i in range(m):
        if arr1[i] - arr2[i] <= 0:
            break
        result += arr1[i] - arr2[i]
    print(result)
else:
    for i in range(n):
        if arr1[i] - arr2[i] <= 0:
            break
        result += arr1[i] - arr2[i]
    print(result)