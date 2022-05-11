import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(start, parent):
    stack = tree[start]
    leaf, temp = True, 1
    for _ in range(len(stack)):
        to = stack.pop()
        if to != parent:
            leaf = False
            temp += dfs(to, start)
    
    if leaf:
        result[start] = 1
        return 1
    else:
        result[start] = temp
        return temp
        

n, r, q = map(int, input().split())
tree = { i + 1 : [] for i in range(n) }
result = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

dfs(r, r)

for _ in range(q):
    print(result[int(input())])