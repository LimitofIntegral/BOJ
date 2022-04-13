import sys
input = sys.stdin.readline

n, m = map(int, input().split())
result = 0

tree = list(map(int, input().split()))

s, e = 0, max(tree)

while s <= e:
    total = 0
    mid = (s + e) // 2

    for i in tree:
        if i > mid:
            total += i - mid

    if total >= m:
        result = mid
        s = mid + 1
    else:
        e = mid - 1

print(result)