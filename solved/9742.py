import sys
sys.setrecursionlimit(10**6)

def fact(n):
    res = 1
    for i in range(n):
        res *= (i + 1)
    return res


def dfs(string="", level=0):
    global step

    if level == l:
        if step == n:
            print(string)
            return True
        else:
            step += 1
            return False

    
    for i in range(l):
        if not check[i]:
            check[i] = 1
            if dfs(string + s[i], level + 1):
                return True
            check[i] = 0


while True:
    try:
        t = list(input().split())
        s, n, step = list(t[0]), int(t[1]), 1
        l = len(s)
        if fact(l) < n:
            print(*t, "= No permutation")
            continue
        check = [0] * l
        print(*t, "= ", end="")
        dfs()

    except EOFError:
        break