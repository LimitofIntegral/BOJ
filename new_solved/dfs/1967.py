import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(start, w = 0, before = -1):
    global result, term

    stack = tree[start][:]

    if len(stack) == 1:
        if stack[0][0] == before:
            if w > result:
                result = w
                term = start
            return
        
    while stack:
        to, to_w = stack.pop()
        if to != before:
            dfs(to, w + to_w, start)

    return


n = int(input())
tree = {i + 1 : [] for i in range(n)}
result, term = 0, 1
for _ in range(n - 1):
    a, b, w = map(int, input().split())
    tree[a].append((b, w))
    tree[b].append((a, w))

dfs(1)
dfs(term)

print(result)