import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(start):
    if check[start]:
        print("CYCLE")
        exit()
    
    check[start] = 1

    for i in graph[start]:
        dfs(i)
    
    check[start] = 0
    return


n = int(input())
graph = [[] for _ in range(n + 1)]
check = [0] * (n + 1)
for i in range(1, n):
    m = int(input())

    if m:
        a = list(map(int, input().split()))

        for j in a:
            graph[i].append(j)
    else:
        _ = input()

dfs(1)
print("NO CYCLE")