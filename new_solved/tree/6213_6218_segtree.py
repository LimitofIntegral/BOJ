import sys
import math
input = sys.stdin.readline

inf = float('inf')

def init(l, r, node):
    if l == r:
        tree[node] = [arr[l], arr[l]]
        return
    else:
        m = (l + r) // 2
        init(l, m, node * 2)
        init(m + 1, r, node * 2 + 1)
        tree[node][0] = max(tree[node * 2][0], tree[node * 2 + 1][0])
        tree[node][1] = min(tree[node * 2][1], tree[node * 2 + 1][1])


def query(l, r, node, li, ri):
    if ri < l or li > r:
        return -inf, inf
    elif li <= l and ri >= r:
        return tree[node]
    elif li <= r or ri >= l:
        m = (l + r) // 2
        a1, a2 = query(l, m, node * 2, li, ri)
        b1, b2 = query(m + 1, r, node * 2 + 1, li, ri)
        return max(a1, b1), min(a2, b2)
n, q = map(int, input().split())
arr = [int(input()) for _ in range(n)]
size = pow(2, math.ceil(math.log(n, 2)) + 1)
tree = [[0, 0] for _ in range(size)]

init(0, n - 1, 1)

for _ in range(q):
    a, b = map(int, input().split())
    t1, t2 = query(0, n - 1, 1, a - 1, b - 1)
    print(t1 - t2)