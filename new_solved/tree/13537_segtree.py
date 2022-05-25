import sys
import math
input = sys.stdin.readline

def merge(a):
    l = len(a)
    if l < 2:
        return a
    
    m = l // 2
    left = merge(a[:m])
    right = merge(a[m:])

    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def count(arr, k):
    l, r, = 0, len(arr) - 1
    result = r

    while l <= r:
        m = (l + r) // 2

        if arr[m] == k:
            l = m + 1
        elif arr[m] > k:
            r = m - 1
        else:
            l = m + 1
    
    return result - l + 1


def init(l, r, n):
    if l == r:
        tree[n] = [arr[l]]
        return tree[n]
    else:
        m = (l + r) // 2
        init(l, m, n * 2)
        init(m + 1, r, n * 2 + 1)
        tree[n] = merge(tree[n * 2] + tree[n * 2 + 1])


def q(l, r, n, li, ri, k):
    if r < li or l > ri:
        return 0
    elif li <= l and ri >= r:
        return count(tree[n], k)
    elif li <= r or ri >= l:
        m = (l + r) // 2
        return q(l, m, n * 2, li, ri, k) + q(m + 1, r, n * 2 + 1, li, ri, k)


n = int(input())
arr = list(map(int, input().split()))
size = pow(2, math.ceil(math.log(n, 2)) + 1)
tree = [None] * size

init(0, n - 1, 1)

for _ in range(int(input())):
    a, b, k = map(int, input().split())
    print(q(0, n - 1, 1, a - 1, b - 1, k))