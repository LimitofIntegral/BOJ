import sys
sys.setrecursionlimit(10**5)

def dfs(n, s=0):
    if n == N:
        check[n].add(s)
        return
    
    check[n].add(s)

    for k in range(4):
        if s + a[k] not in check[n + 1]:
            dfs(n + 1, s + a[k])


a = [1, 5, 10, 50]
N = int(input())
check = [set() for _ in range(N + 1)]
dfs(0)

print(len(check[N]))