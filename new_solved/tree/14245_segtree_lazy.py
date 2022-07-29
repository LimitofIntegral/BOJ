import sys, math
input = sys.stdin.readline

def init(l, r, n):
    if l == r:
        tree[n] = arr[l]
    else:
        m = (l + r) // 2
        init(l, m, n * 2)
        init(m + 1, r, n * 2 + 1)


def prop(l, r, n):
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
        tree[n] ^= v
        if l != r:
            lazy[n * 2] ^= v
            lazy[n * 2 + 1] ^= v
        return
    elif li <= r or ri >= l:
        m = (l + r) // 2
        update(l, m, n * 2, li, ri, v)
        update(m + 1, r, n * 2 + 1, li, ri, v)


def query(l, r, n, i):
    prop(l, r, n)
    if l == r == i:
        return tree[n]
    else:
        m = (l + r) // 2
        if i <= m:
            return query(l, m, n * 2, i)
        else:
            return query(m + 1, r, n * 2 + 1, i)


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
        print(query(0, n - 1, 1, c[1]))