import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(start, w = 0, before = -1):
    global result, term

    stack = tree[start].copy()

    if len(stack) == 1:
        for i in stack:
            if i == before:
                if w > result:
                    result = w
                    term = start
                return

    for i in stack:
        to, to_w = i, stack[i]
        if to != before:
            dfs(to, w + to_w, start)
    
    return
    

n = int(input())
tree = {i + 1 : {} for i in range(n)}
result, term = 0, 1
for _ in range(n):
    temp = list(map(int, input().split()))
    for i in range((len(temp) - 2) // 2):
        tree[temp[0]][temp[i * 2 + 1]] = temp[i * 2 + 2]
        tree[temp[i * 2 + 1]][temp[0]] = temp[i * 2 + 2]

dfs(1)
dfs(term)

print(result)