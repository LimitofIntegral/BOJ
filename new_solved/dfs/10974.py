def dfs(level):
    if level == n:
        print(*result)
        return
    for i in range(n):
        if check[i]:
            continue
        check[i] = True
        result[level] = arr[i]
        dfs(level + 1)
        check[i] = False

n = int(input())



arr = [i + 1 for i in range(n)]
result = [0] * n
check = [False] * n

dfs(0)