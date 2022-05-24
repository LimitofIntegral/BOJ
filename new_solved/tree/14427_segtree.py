import sys
import math as m
input = sys.stdin.readline

def init(l, r, node):
    if l == r:
        tree[node] = [l + 1, arr[l]]
        return
    else:
        m = (l + r) // 2
        init(l, m, node * 2)
        init(m + 1, r, node * 2 + 1)
        if tree[node * 2][1] < tree[node * 2 + 1][1]:
            tree[node] = tree[node * 2]
        elif tree[node * 2][1] == tree[node * 2 + 1][1]:
            if tree[node * 2][0] <= tree[node * 2 + 1][0]:
                tree[node] = tree[node * 2]
            else:
                tree[node] = tree[node * 2 + 1]
        else:
            tree[node] = tree[node * 2 + 1]


def update(l, r, node, i, v):
    if l == r == i:
        tree[node][1] = v
        return tree[node]
    if i < l or i > r:
        return [0, float('inf')]
    else:
        m = (l + r) // 2
        update(l, m, node * 2, i, v)
        update(m + 1, r, node * 2 + 1, i, v)
        if tree[node * 2][1] < tree[node * 2 + 1][1]:
            tree[node] = tree[node * 2]
        elif tree[node * 2][1] == tree[node * 2 + 1][1]:
            if tree[node * 2][0] <= tree[node * 2 + 1][0]:
                tree[node] = tree[node * 2]
            else:
                tree[node] = tree[node * 2 + 1]
        else:
            tree[node] = tree[node * 2 + 1]


n = int(input())
arr = list(map(int, input().split()))

size = pow(2, m.ceil(m.log(n, 2)) + 1)
tree = [[0, float('inf')]] * size

init(0, n - 1, 1)

for _ in range(int(input())):
    cmd = input().strip()
    if cmd == "2":
        print(tree[1][0])
    else:
        _, i, v = map(int, cmd.split())
        update(0, n - 1, 1, i - 1, v)