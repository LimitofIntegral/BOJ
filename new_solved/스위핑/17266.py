import sys
input = sys.stdin.readline


n = int(input())
m = int(input())
arr = list(map(int, input().split()))

l, r = 0, 200000
res = 0

while l <= r:
    end = 0
    m = (l + r) // 2
    check = True

    for i in arr:
        if i - m <= end:
            end = i + m
        else:
            check = False
            break
    
    if check and end >= n:
        res = m
        r = m - 1
    else:
        l = m + 1

print(res)
