def dfs(level):
    if level == m:
        print(*result[1:])
        return
    for i in range(n):
        if result[level] <= arr[i]:
            result[level + 1] = arr[i]
        else:
            continue
        dfs(level + 1)


n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = [0] * (m + 1)

dfs(0)