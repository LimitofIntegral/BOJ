import sys
import math as m
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
    global result
    if ri < l or li > r:
        return
    elif li <= l and ri >= r:
        result += tree[node]
        return
    elif li <= r or ri >= l:
        m = (l + r) // 2
        query(l, m, node * 2, li, ri)
        query(m + 1, r, node * 2 + 1, li, ri)
        return


n, q = map(int, input().split())
arr = list(map(int, input().split()))

size = pow(2, m.ceil(m.log(len(arr), 2)) + 1)
tree = [0] * size

init(0, n - 1, 1)

for _ in range(q):
    result = 0
    x, y, a, b = map(int, input().split())
    if x > y:
        x, y = y, x
    query(0, n - 1, 1, x - 1, y - 1)
    print(result)
    update(0, n - 1, 1, a - 1, b)
