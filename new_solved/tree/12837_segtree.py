import sys
import math
input = sys.stdin.readline

def up(l, r, n, i, v):
    if l == r == i:
        tree[n] += v
        return v
    if i < l or i > r:
        return 0
    else:
        m = (l + r) // 2
        up(l, m, n * 2, i, v)
        up(m + 1, r, n * 2 + 1, i, v)
        tree[n] = tree[n * 2] + tree[n * 2 + 1]


def query(l, r, n, li, ri):
    if r < li or l > ri:
        return 0
    elif li <= l and ri >= r:
        return tree[n]
    elif li <= r or ri >= l:
        m = (l + r) // 2
        return query(l, m, n * 2, li, ri) + query(m + 1, r, n * 2 + 1, li, ri)


n, q = map(int, input().split())
size = pow(2, math.ceil(math.log(n, 2)) + 1)
tree = [0] * size

for _ in range(q):
    c, a, b = map(int, input().split())
    if c == 1:
        up(0, n - 1, 1, a - 1, b)
    else:
        print(query(0, n - 1, 1, a - 1, b - 1))