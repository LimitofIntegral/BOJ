def dfs(start, parent):
    stack = tree[start]
    leaf, result = True, 0
    for _ in range(len(stack)):
        to = stack.pop()
        if to != parent:
            leaf = False
            result += dfs(to, start)
    
    if leaf:
        return 1
    else:
        return result


n = int(input())
arr = list(map(int, input().split()))
x = int(input())
tree = { i : [] for i in range(n) }
root = None
for node, to in enumerate(arr):
    if to == -1:
        root = node
        continue

    if node == x or to == x:
        continue
    
    tree[node].append(to)
    tree[to].append(node)


print(0 if root == x else dfs(root, root))