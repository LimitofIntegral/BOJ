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
        tree[n] = max(tree[n * 2], tree[n * 2 + 1])


def q(l, r, n, li, ri):
    if ri < l or li > r:
        return 0
    elif li <= l and ri >= r:
        return tree[n]
    elif li <= r or ri >= l:
        m = (l + r) // 2
        return max(q(l, m, n * 2, li, ri), q(m + 1, r, n * 2 + 1, li, ri))


n, m = map(int, input().split())
arr = list(map(int, input().split()))
size = pow(2, math.ceil(math.log(n, 2)) + 1)
tree = [0] * size

init(0, n - 1, 1)

for i in range(m - 1, n - m + 1):
    if i != n - m:
        print(q(0, n - 1, 1, i - m + 1, i + m - 1), end = " ")
    else:
        print(q(0, n - 1, 1, i - m + 1, i + m - 1))