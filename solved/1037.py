N = int(input())
arr = list(map(int, input().split()))

print(arr[0] ** 2 if len(arr) == 1 else min(arr) * max(arr))