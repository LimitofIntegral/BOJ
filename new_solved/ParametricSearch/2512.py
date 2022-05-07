n = int(input())
arr = list(map(int, input().split()))
g = int(input())
result = 0

if sum(arr) <= g:
    print(max(arr))
else:
    s, e = 0, max(arr)
    while s <= e:
        total = 0
        m = (e + s) // 2

        for i in arr:
            if i < m:
                total += i
            else:
                total += m

        if total <= g:
            s = m + 1
            result = m
        else:
            e = m - 1

    print(result)
