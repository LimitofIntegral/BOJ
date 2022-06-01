def func(pl, pr, il, ir):
    if pl > pr or il > ir:
        return
    root = ord(pre[pl]) - 64
    m = node[root]

    left = m - il
    right = ir - m
    func(pl + 1, pl + left, il, il + left - 1)
    func(pr - right + 1, pr, ir - right + 1, ir)
    print(chr(root + 64), end = "")


while True:
    try:
        a, b = input().split()
        pre = list(a)
        in_ = list(b)
        n = len(pre)
        node = [0] * (n + 1)
        for i in range(n):
            node[ord(in_[i]) - 64] = i

        func(0, n - 1, 0, n - 1)
        print()
    except EOFError:
        break
