def dfs(level):
    if level == m + 1:
        print(*result[1:])
        return
    for i in range(n):
        if result[level - 1] <= arr[i]:
            result[level] = arr[i]
            dfs(level + 1)

n, m = map(int, input().split())
result = [0] * (m + 1)
arr = list(set(map(int, input().split())))
arr.sort()
n = len(arr)

dfs(1)