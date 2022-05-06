def dfs(i):
    if visited[i]:
        return
    visited[i] = True
    step = arr[i]
    if i - step >= 0:
        dfs(i - step)
    if i + step < n:
        dfs(i + step)

n = int(input())
visited = [False] * n
result = 0
arr = list(map(int, input().split()))
s = int(input())

dfs(s - 1)

for i in visited:
    if i:
        result += 1

print(result)