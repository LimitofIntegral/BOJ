from cmath import inf
import sys
import math
input = sys.stdin.readline

def init(l, r, n):
    if l == r:
        tree[n] = arr[l]
        return
    else:
        m = (l + r) // 2
        init(l, m, n * 2)
        init(m + 1, r, n * 2 + 1)
        tree[n] = min(tree[n * 2], tree[n * 2 + 1])


def up(l, r, n, i, v):
    if l == r == i:
        tree[n] = v
        return v
    if i < l or i > r:
        return float('inf')
    else:
        m = (l + r) // 2
        up(l, m, n * 2, i, v)
        up(m + 1, r, n * 2 + 1, i, v)
        tree[n] = min(tree[n * 2], tree[n * 2 + 1])


def q(l, r, n, li, ri):
    if ri < l or li > r:
        return float('inf')
    elif li <= l and ri >= r:
        return tree[n]
    elif li <= r or ri >= l:
        m = (l + r) // 2
        return min(q(l, m, n * 2, li, ri), q(m + 1, r, n * 2 + 1, li, ri))


n = int(input())
arr = list(map(int, input().split()))
size = pow(2, math.ceil(math.log(n, 2)) + 1)
tree = [0] * size

init(0, n - 1, 1)


for _ in range(int(input())):
    c, a, b = map(int, input().split())
    if c == 1:
        up(0, n - 1, 1, a - 1, b)
    else:
        print(q(0, n - 1, 1, a - 1, b - 1))