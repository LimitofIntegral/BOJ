import sys
import math


def init(l, r, n):
    if l == r:
        if arr[l] > 0:
            tree[n] = 1
        elif arr[l] == 0:
            tree[n] = 0
        else:
            tree[n] = -1
        return
    else:
        m = (l + r) // 2
        init(l, m, n * 2)
        init(m + 1, r, n * 2 + 1)
        tree[n] = tree[n * 2] * tree[n * 2 + 1]


def up(l, r, n, i, v):
    if l == r == i:
        if v > 0:
            tree[n] = 1
        elif v == 0:
            tree[n] = 0
        else:
            tree[n] = -1
        return tree[n]
    if i < l or i > r:
        return 1
    else:
        m = (l + r) // 2
        up(l, m, n * 2, i, v)
        up(m + 1, r, n * 2 + 1, i, v)
        tree[n] = tree[n * 2] * tree[n * 2 + 1]


def q(l, r, n, li, ri):
    if ri < l or li > r:
        return 1
    elif li <= l and ri >= r:
        return tree[n]
    elif li <= r or ri >= l:
        m = (l + r) // 2
        return q(l, m, n * 2, li, ri) * q(m + 1, r, n * 2 + 1, li, ri)


while True:
    try:
        n, k = map(int, input().split())
        arr = list(map(int, sys.stdin.readline().split()))
        size = pow(2, math.ceil(math.log(n, 2)) + 1)
        tree = [None] * size

        init(0, n - 1, 1)

        for i in range(k):
            c, a, b = sys.stdin.readline().split()
            a, b = int(a), int(b)
            if c == "C":
                up(0, n - 1, 1, a - 1, b)
            else:
                p = q(0, n - 1, 1, a - 1, b - 1)
                if p > 0:
                    print("+", end = "")
                elif p == 0:
                    print(0, end = "")
                else:
                    print("-", end = "")
            if i == k - 1:
                print()
    except EOFError:
        break
