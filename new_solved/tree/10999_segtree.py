import sys
import math
input = sys.stdin.readline

def init(l, r, n):
    if l == r:
        tree[n] = arr[l]
    else:
        m = (l + r) // 2
        init(l, m, n * 2)
        init(m + 1, r, n * 2 + 1)
        tree[n] = tree[n * 2] + tree[n * 2 + 1]


def query(l, r, n, li, ri):
    prop(l, r, n)
    if ri < l or li > r:
        return 0
    elif li <= l and ri >= r:
        return tree[n]
    elif li <= r or ri >= l:
        m = (l + r) // 2
        return query(l, m, n * 2, li, ri) + query(m + 1, r, n * 2 + 1, li, ri)


def prop(l, r, n):
    tree[n] += (r - l + 1) * lazy[n]
    if l != r:
        lazy[n * 2] += lazy[n]
        lazy[n * 2 + 1] += lazy[n]
    lazy[n] = 0


def update(l, r, n, li, ri, v):
    prop(l, r, n)
    if ri < l or li > r:
        return
    elif li <= l and ri >= r:
        tree[n] += (r - l + 1) * v
        if l != r:
            lazy[n * 2] += v
            lazy[n * 2 + 1] += v
        return
    elif li <= r or ri >= l:
        m = (l + r) // 2
        update(l, m, n * 2, li, ri, v)
        update(m + 1, r, n * 2 + 1, li, ri, v)
        tree[n] = tree[n * 2] + tree[n * 2 + 1]


n, m, k = map(int, input().split())
size = pow(2, math.ceil(math.log(n, 2)) + 1)

tree, lazy = [0] * size, [0] * size
arr = [int(input()) for _ in range(n)]

init(0, n - 1, 1)

for _ in range(m + k):
    c = list(map(int, input().split()))
    
    if len(c) == 4:
        update(0, n - 1, 1, c[1] - 1, c[2] - 1, c[3])
    else:
        print(query(0, n - 1, 1, c[1] - 1, c[2] - 1))