import sys
import math
input = sys.stdin.readline

inf = float('inf')

def init(l, r, node):
    if l == r:
        tree[node] = arr[l]
        return
    else:
        m = (l + r) // 2
        init(l, m, node * 2)
        init(m + 1, r, node * 2 + 1)
        tree[node] = min(tree[node * 2], tree[node * 2 + 1])


def query(l, r, node, li, ri):
    if ri < l or li > r:
        return inf
    elif li <= l and ri >= r:
        return tree[node]
    elif li <= r or ri >= l:
        m = (l + r) // 2
        return min(query(l, m, node * 2, li, ri), query(m + 1, r, node * 2 + 1, li, ri))


n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
size = pow(2, math.ceil(math.log(n, 2)) + 1)
tree = [inf] * size
init(0, n - 1, 1)

for _ in range(m):
    a, b = map(int, input().split())
    print(query(0, n - 1, 1, a - 1, b - 1))