import sys
sys.setrecursionlimit(50)

def dfs(n, step=0, visited=[]):
    global result, arr
    visited.append(n)

    if n == 1:
        if step < result:
            result = step
            arr = visited[:]
        visited.pop()
        return
    
    if step == result:
        visited.pop()
        return
    
    if not n % 3:
        dfs(n // 3, step + 1, visited)
    if not n % 2:
        dfs(n // 2, step + 1, visited)
    dfs(n - 1, step + 1, visited)
    visited.pop()
    return


n = int(input())
result = float('inf')
arr = []
dfs(n)
print(result)
print(*arr)