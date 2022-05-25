import sys
import math
input = sys.stdin.readline

def init(l, r, n):
    if l == r:
        if arr[l] % 2:
            tree[n] = [0, 1]
        else:
            tree[n] = [1, 0]
        return
    else:
        m = (l + r) // 2
        init(l, m, n * 2)
        init(m + 1, r, n * 2 + 1)
        tree[n] = [tree[n * 2][0] + tree[n * 2 + 1][0], tree[n * 2][1] + tree[n * 2 + 1][1]]


def up(l, r, n, i, v):
    if l == r == i:
        if v % 2:
            tree[n] = [0, 1]
        else:
            tree[n] = [1, 0]
        return tree[n]
    if i < l or i > r:
        return [0, 0]
    else:
        m = (l + r) // 2
        up(l, m, n * 2, i, v)
        up(m + 1, r, n * 2 + 1, i, v)
        tree[n] = [tree[n * 2][0] + tree[n * 2 + 1][0], tree[n * 2][1] + tree[n * 2 + 1][1]]


def q(l, r, n, li, ri):
    if li > r or ri < l:
        return [0, 0]
    elif li <= l and ri >= r:
        return tree[n]
    elif li <= r or ri >= l:
        m = (l + r) // 2
        t1 = q(l, m, n * 2, li, ri)
        t2 = q(m + 1, r, n * 2 + 1, li, ri)
        return [t1[0] + t2[0], t1[1] + t2[1]]


n = int(input())
arr = list(map(int, input().split()))
size = pow(2, math.ceil(math.log(n, 2)) + 1)
tree = [None] * size

init(0, n - 1, 1)

for _ in range(int(input())):
    c, a, b = map(int, input().split())
    if c == 1:
        up(0, n - 1, 1, a - 1, b)
    elif c == 2:
        print(q(0, n - 1, 1, a - 1, b - 1)[0])
    else:
        print(q(0, n - 1, 1, a - 1, b - 1)[1])