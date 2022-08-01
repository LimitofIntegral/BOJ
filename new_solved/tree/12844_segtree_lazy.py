import sys, math
input = sys.stdin.readline

def init(l, r, n):
    if l == r:
        tree[n] = arr[l]
        return tree[n]
    else:
        m = (l + r) // 2
        tree[n] = init(l, m, n * 2) ^ init(m + 1, r, n * 2 + 1)
        return tree[n]
        

def prop(l, r, n):
    if (r - l + 1) % 2:
        tree[n] ^= lazy[n]
    if l != r:
        lazy[n * 2] ^= lazy[n]
        lazy[n * 2 + 1] ^= lazy[n]
    lazy[n] = 0


def update(l, r, n, li, ri, v):
    prop(l, r, n)
    if ri < l or li > r:
        return
    elif li <= l and ri >= r:
        if (r - l + 1) % 2:
            tree[n] ^= v
        if l != r:
            lazy[n * 2] ^= v
            lazy[n * 2 + 1] ^= v
        return
    m = (l + r) // 2
    update(l, m, n * 2, li, ri, v)
    update(m + 1, r, n * 2 + 1, li, ri, v)
    tree[n] = tree[n * 2] ^ tree[n * 2 + 1]


def query(l, r, n, li, ri):
    prop(l, r, n)
    if ri < l or li > r:
        return 0
    elif li <= l and ri >= r:
        return tree[n]
    m = (l + r) // 2
    return query(l, m, n * 2, li, ri) ^ query(m + 1, r, n * 2 + 1, li, ri)


n = int(input())
size = pow(2, math.ceil(math.log(n, 2)) + 1)
tree, lazy = [0] * size, [0] * size

arr = list(map(int, input().split()))

init(0, n - 1, 1)

for _ in range(int(input())):
    c = list(map(int, input().split()))
    if c[0] == 1:
        update(0, n - 1, 1, c[1], c[2], c[3])
    else:
        print(query(0, n - 1, 1, c[1], c[2]))