import sys
import math
input = sys.stdin.readline

inf = float('inf')

def init(l, r, node):
    if l == r:
        tree[node][0] = arr[l]
        tree[node][1] = arr[l]
    else:
        m = (l + r) // 2
        init(l, m, node * 2)
        init(m + 1, r, node * 2 + 1)
        tree[node][0] = min(tree[node * 2][0], tree[node * 2 + 1][0])
        tree[node][1] = max(tree[node * 2][1], tree[node * 2 + 1][1])


def query(l, r, node, li, ri):
    global r1, r2
    if ri < l or li > r:
        return
    elif li <= l and ri >= r:
        r1 = min(r1, tree[node][0])
        r2 = max(r2, tree[node][1])
    elif li <= r or ri >= l:
        m = (l + r) // 2
        query(l, m, node * 2, li, ri)
        query(m + 1, r, node * 2 + 1, li, ri)
        return
    

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
size = pow(2, math.ceil(math.log(n, 2)) + 1)
tree = [[inf, -inf] for _ in range(size)]

init(0, n - 1, 1)

for _ in range(m):
    r1, r2 = inf, -inf
    a, b = map(int, input().split())
    query(0, n - 1, 1, a - 1, b - 1)
    print(r1, r2)