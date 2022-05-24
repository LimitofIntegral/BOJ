import sys
import math
input = sys.stdin.readline

inf = float('inf')

def init(l, r, n):
    if l == r:
        tree[n] = [l + 1, arr[l]]
        return
    else:
        m = (l + r) // 2
        init(l, m, n * 2)
        init(m + 1, r, n * 2 + 1)
        if tree[n * 2][1] < tree[n * 2 + 1][1]:
            tree[n][0] = tree[n * 2][0]
            tree[n][1] = tree[n * 2][1]
            return
        if tree[n * 2][1] == tree[n * 2 + 1][1]:
            if tree[n * 2][0] < tree[n * 2 + 1][0]:
                tree[n][0] = tree[n * 2][0]
                tree[n][1] = tree[n * 2][1]
                return
        tree[n][0] = tree[n * 2 + 1][0]
        tree[n][1] = tree[n * 2 + 1][1]
        return


def up(l, r, n, i, v):
    if l == r == i:
        tree[n][1] = v
        return tree[n]
    if i < l or i > r:
        return [inf, inf]
    else:
        m = (l + r) // 2
        up(l, m, n * 2, i, v)
        up(m + 1, r, n * 2 + 1, i, v)
        if tree[n * 2][1] < tree[n * 2 + 1][1]:
            tree[n][0] = tree[n * 2][0]
            tree[n][1] = tree[n * 2][1]
            return
        if tree[n * 2][1] == tree[n * 2 + 1][1]:
            if tree[n * 2][0] < tree[n * 2 + 1][0]:
                tree[n][0] = tree[n * 2][0]
                tree[n][1] = tree[n * 2][1]
                return
        tree[n][0] = tree[n * 2 + 1][0]
        tree[n][1] = tree[n * 2 + 1][1]
        return


def q(l, r, n, li, ri):
    if r < li or l > ri:
        return [inf, inf]
    elif li <= l and ri >= r:
        return tree[n]
    elif li <= r or ri >= l:
        m = (l + r) // 2
        ai, av = q(l, m, n * 2, li, ri)
        bi, bv = q(m + 1, r, n * 2 + 1, li, ri)
        if av < bv:
            return [ai, av]
        elif av == bv:
            if ai < bi:
                return [ai, av]
        return [bi, bv]


n = int(input())
arr = list(map(int, input().split()))
size = pow(2, math.ceil(math.log(n, 2)) + 1)
tree = [[0, 0] for _ in range(size)]

init(0, n - 1, 1)

for _ in range(int(input())):
    c, a, b = map(int, input().split())
    if c == 1:
        up(0, n - 1, 1, a - 1, b)
    else:
        result, _ = q(0, n - 1, 1, a - 1, b - 1)
        print(result)