import sys, random
from math import gcd
sys.setrecursionlimit(10 ** 5)

def f(x, c, n):
    return (x ** 2 % n + c + n) % n 


def power(x, y, mod):
    r = 1
    x %= mod
    while y > 0:
        if y & 1:
            r = (r * x) % mod
        y >>= 1
        x = x ** 2 % mod
    return r


def mr(n, a):
    r = 0
    d = n - 1
    while not d % 2:
        r += 1
        d //= 2
    
    x = power(a, d, n)
    if x == 1 or x == n - 1:
        return True
    
    for i in range(r - 1):
        x = power(x, 2, n)
        if x == n - 1:
            return True
    return False


def is_prime(n):
    p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    if n == 1:
        return False
    if n in (2, 3):
        return True
    if not n % 2:
        return False
    
    for i in p:
        if n == i:
            return True
        if not mr(n, i):
            return False
    
    return True


def pr(n):
    if is_prime(n):
        return n
    if n == 1:
        return 1
    if not n % 2:
        return 2
    
    x = random.randint(2, n)
    y = x
    c = random.randint(1, n)
    g = 1

    while g == 1:
        x = f(x, c, n)
        y = f(y, c, n)
        y = f(y, c, n)
        g = gcd(abs(x - y), n)

        if g == n:
            return pr(n)
    
    if is_prime(g):
        return g
    else:
        return pr(g)


n = int(input())
res = []
while n > 1:
    d = pr(n)
    res.append(d)
    n //= d

for i in sorted(res):
    print(i)