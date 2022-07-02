import sys
input = sys.stdin.readline
 
n = int(input())
tree = [[-1 for _ in range(2)] for _ in range(n + 1)]
for i in range(1, n + 1):
    a, b = map(int, input().split())
    tree[i][0] = a
    tree[i][1] = b
 
k = int(input())
node = 1

while k >= 0:
    check = k % 2

    if tree[node][0] == -1 and tree[node][1] == -1:
        break
    else:
        if tree[node][0] == -1:
            node = tree[node][1]
        elif tree[node][1] == -1:
            node = tree[node][0]
        else:
            if check:
                node = tree[node][0]
            else:
                node = tree[node][1]
            k = k // 2 + check
 
print(node)