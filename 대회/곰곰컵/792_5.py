import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(start):
    if start in d:
        return False
        
    stack = graph[start]

    if stack:
        l = len(stack)
        result = [True] * l
        for i in range(l):
            if stack[i] in d:
                result[i] = False
            else:
                result[i] = dfs(stack[i])
        if True in result:
            return True
    else:
        return True


n, m = map(int, input().split())
graph = {i + 1 : [] for i in range(n)}

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

s = int(input())
d = {i : None for i in list(map(int, input().split()))}

if dfs(1):
    print("yes")
else:
    print("Yes")