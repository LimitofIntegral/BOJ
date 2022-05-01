def dfs(level):
    if level == m:
        print(*result)
        return
    for i in range(n):
        if check[i]:
            continue
        result[level] = arr[i]
        check[i] = True
        dfs(level + 1)
        check[i] = False

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
check = [False] * n
result = [0] * m
dfs(0)