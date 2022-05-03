def string(arr):
    temp = ""
    for i in arr:
        temp += str(i)
    return temp

def dfs(level):
    if level == m:
        temp = string(result)
        if temp not in d:
            d[temp] = None
            print(*result)
        return
    for i in range(n):
        if check[i]:
            continue
        check[i] = True
        result[level] = arr[i]
        dfs(level + 1)
        check[i] = False


n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = [0] * m
check = [False] * n
d = {}

dfs(0)