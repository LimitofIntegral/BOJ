import sys, math

from pyrsistent import v
input = sys.stdin.readline

def prop(l, r, n):
    tree[n] += (r - l + 1) * lazy[n]
    if l != r:
        lazy[n * 2] += lazy[n]
        lazy[n * 2 + 1] += lazy[n]
    lazy[n] = 0


def update(l, r, n, li, ri):
    if lazy[n]:
        prop(l, r, n)
    if ri < l or li >r:
        return
    elif li <= l and ri >= r:
        tree[n] += (r - l + 1)
        if l != r:
            lazy[n * 2] += 1
            lazy[n * 2 + 1] += 1
        return
    m = (l + r) // 2
    update(l, m, n * 2, li, ri)
    update(m + 1, r, n * 2 + 1, li, ri)
    tree[n] = tree[n * 2] + tree[n * 2 + 1]


def query(l, r, n, li, ri):
    if lazy[n]:
        prop(l, r, n)
    if ri < l or li > r:
        return 0
    elif li <= l and ri >= r:
        return tree[n]
    m = (l + r) // 2
    return query(l, m, n * 2, li, ri) + query(m + 1, r, n * 2 + 1, li, ri)


n = int(input())
size = pow(2, math.ceil(math.log(86400, 2)) + 1)

tree, lazy = [0] * size, [0] * size

for _ in range(n):
    a, b = input().split(" - ")
    a, b = list(map(int, a.split(":"))), list(map(int, b.split(":")))

    l = a[0] * 3600 + a[1] * 60 + a[2]
    r = b[0] * 3600 + b[1] * 60 + b[2]

    if l <= r:
        update(0, 86399, 1, l, r)
    else:
        update(0, 86399, 1, l, 86399)
        update(0, 86399, 1, 0, r)

for _ in range(int(input())):
    a, b = input().split(" - ")
    a, b = list(map(int, a.split(":"))), list(map(int, b.split(":")))

    l = a[0] * 3600 + a[1] * 60 + a[2]
    r = b[0] * 3600 + b[1] * 60 + b[2]

    if l <= r:
        res = query(0, 86399, 1, l, r) / (r - l + 1)
        print(res)
    else:
        res = query(0, 86399, 1, l, 86399)
        res += query(0, 86399, 1, 0, r)
        print(res / (86401 + r - l))