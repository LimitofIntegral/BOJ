import sys
import math
input = sys.stdin.readline

def init(l, r, node):
    if l == r:
        tree[node] = arr[l]
        return
    else:
        m = (l + r) // 2
        init(l, m, node * 2)
        init(m + 1, r, node * 2 + 1)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]


def update(l, r, node, i, v):
    if l == r == i:
        tree[node] = v
        return tree[node]
    if i < l or i > r:
        return 0
    else:
        m = (l + r) // 2
        update(l, m, node * 2, i, v)
        update(m + 1, r, node * 2 + 1, i, v)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]


def query(l, r, node, li, ri):
    if ri < l or li > r:
        return 0
    elif li <= l and ri >= r:
        return tree[node]
    elif li <= r or ri >= l:
        m = (l + r) // 2
        return query(l, m, node * 2, li, ri) + query(m + 1, r, node * 2 + 1, li, ri)


n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
size = pow(2, math.ceil(math.log(n, 2)) + 1)
tree = [0] * size
init(0, n - 1, 1)

for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(0, n - 1, 1, b - 1, c)
    else:
        print(query(0, n - 1, 1, b - 1, c - 1))
        