import sys
import math
input = sys.stdin.readline

def update(l, r, node, i, v):
    if l == r == i:
        tree[node] = v
        return
    if i < l or i > r:
        return
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


n, m = map(int, input().split())
size = pow(2, math.ceil(math.log(n, 2)) + 1)
tree = [0] * size

for _ in range(m):
    a, b, c = map(int, input().split())
    if a:
        update(0, n - 1, 1, b - 1, c)
    else:
        if b > c:
            b, c = c, b
        print(query(0, n - 1, 1, b - 1, c - 1))