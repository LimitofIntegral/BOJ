import sys
input = sys.stdin.readline

def func(pl, pr, il, ir):
    if pl > pr or il > ir:
        return
    root = pre[pl]
    m = node[root]

    left = m - il
    right = ir - m
    func(pl + 1, pl + left, il, il + left - 1)
    func(pr - right + 1, pr, ir - right + 1, ir)
    print(root, end = " ")


for _ in range(int(input())):
    n = int(input())
    pre = list(map(int, input().split()))
    in_ = list(map(int, input().split()))
    node = [0] * (n + 1)
    for i in range(n):
        node[in_[i]] = i

    func(0, n - 1, 0, n - 1)
    print()

