n = int(input())
k = int(input())

l, r, result = 1, k, 0

while l <= r:
    count = 0
    m = (l + r) // 2
    for i in range(1, n + 1):
        count += min(m // i, n)
    if count < k:
        l = m + 1
    else:
        result, r = m, m - 1

print(result)