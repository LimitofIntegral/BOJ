import sys, math
input = sys.stdin.readline

def init(l, r, n):
    if l == r:
        tree[n][0], tree[n][1] = arr[l], arr[l]
        return
    else:
        m = (l + r) // 2
        init(l, m, n * 2)
        init(m + 1, r, n * 2 + 1)
        tree[n][0] = tree[n * 2][0] + tree[n * 2 + 1][0]
        tree[n][1] = min(tree[n * 2][1], tree[n * 2 + 1][1])


def prop(l, r, n):
    tree[n][0] += (r - l + 1) * lazy[n]
    tree[n][1] += lazy[n]
    if l != r:
        lazy[n * 2] += lazy[n]
        lazy[n * 2 + 1] += lazy[n]
    lazy[n] = 0


def update(l, r, n, li, ri, v):
    prop(l, r, n)
    if ri < l or li > r:
        return
    elif li <= l and ri >= r:
        tree[n][0] += (r - l + 1) * v
        tree[n][1] += v
        if l != r:
            lazy[n * 2] += v
            lazy[n * 2 + 1] += v
        return
    m = (l + r) // 2
    update(l, m, n * 2, li, ri, v)
    update(m + 1, r, n * 2 + 1, li, ri, v)
    tree[n][0] = tree[n * 2][0] + tree[n * 2 + 1][0]
    tree[n][1] = min(tree[n * 2][1], tree[n * 2 + 1][1])


def query(l, r, n, li, ri):
    prop(l, r, n)
    if ri < l or li > r:
        return 0, float('inf')
    elif li <= l and ri >= r:
        return tree[n]
    m = (l + r) // 2
    left = query(l, m, n * 2, li, ri)
    right = query(m + 1, r, n * 2 + 1, li, ri)
    return left[0] + right[0], min(left[1], right[1])


n, q = map(int, input().split())
size = pow(2, math.ceil(math.log(n, 2)) + 1)
tree, lazy = [[0, float('inf')] for _ in range(size)], [0] * size

arr = list(map(int, input().split()))

init(0, n - 1, 1)

for _ in range(q):
    c = input().split()
    
    if c[0] == "M":
        print(query(0, n - 1, 1, int(c[1]) - 1, int(c[2]) - 1)[1])
    elif c[0] == "S":
        print(query(0, n - 1, 1, int(c[1]) - 1, int(c[2]) - 1)[0])
    else:
        update(0, n - 1, 1, int(c[1]) - 1, int(c[2]) - 1, int(c[3]))