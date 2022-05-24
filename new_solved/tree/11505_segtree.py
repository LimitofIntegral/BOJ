import sys
import math
input = sys.stdin.readline

def init(l, r, node):
    if l == r:
        tree[node] = arr[l] % 1000000007
        return
    else:
        m = (l + r) // 2
        init(l, m, node * 2)
        init(m + 1, r, node * 2 + 1)
        tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % 1000000007


def up(l, r, node, i, v):
    if l == r == i:
        tree[node] = v
        return v
    if i < l or i > r:
        return 1
    else:
        m = (l + r) // 2
        up(l, m, node * 2, i, v)
        up(m + 1, r, node * 2 + 1, i, v)
        tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % 1000000007


def query(l, r, node, li, ri):
    global result
    if ri < l or li > r:
        return
    elif li <= l and ri >= r:
        result *= tree[node]
        result %= 1000000007
        return
    elif li <= r or ri >= l:
        m = (l + r) // 2
        query(l, m, node * 2, li, ri)
        query(m + 1, r, node * 2 + 1, li, ri)
        return


n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

size = pow(2, math.ceil(math.log(n, 2)) + 1)
tree = [0] * size

init(0, n - 1, 1)

for _ in range(m + k):
    c, a, b = map(int, input().split())
    if c == 1:
        up(0, n - 1, 1, a - 1, b)
    else:
        result = 1
        query(0, n - 1, 1, a - 1, b - 1)
        print(result)
    