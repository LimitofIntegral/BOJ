import sys, math
input = sys.stdin.readline

def init(l, r, n):
    if l == r:
        tree[n] = arr[l]
        return
    else:
        m = (l + r) // 2
        init(l, m, n * 2)
        init(m + 1, r, n * 2 + 1)
        tree[n] = tree[n * 2] + tree[n * 2 + 1]


def prop(l, r, n):
    tree[n] += (r - l + 1) * lazy[n]
    if l != r:
        lazy[n * 2] += lazy[n]
        lazy[n * 2 + 1] += lazy[n]
    lazy[n] = 0


def query(l, r, n, li, ri):
    prop(l, r, n)
    if ri < l or li > r:
        return 0
    elif li <= l and ri >= r:
        return tree[n]
    m = (l + r) // 2
    return query(l, m, n * 2, li, ri) + query(m + 1, r, n * 2 + 1, li, ri)


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
    m = (l + r) // 2
    update(l, m, n * 2, li, ri, v)
    update(m + 1, r, n * 2 + 1, li, ri, v)
    tree[n] = tree[n * 2] + tree[n * 2 + 1]


n, q1, q2 = map(int, input().split())
size = pow(2, math.ceil(math.log(n, 2)) + 1)
tree, lazy = [0] * size, [0] * size

arr = list(map(int, input().split()))

init(0, n - 1, 1)

for _ in range(q1 + q2):
    c = list(map(int, input().split()))
    if c[0] == 1:
        print(query(0, n - 1, 1, c[1] - 1, c[2] - 1))
    else:
        update(0, n - 1, 1, c[1] - 1, c[2] - 1, c[3])