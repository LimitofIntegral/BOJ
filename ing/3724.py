for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = []
    for _ in range(m):
        arr.append(list(map(int, input().split())))
    result, r = -1, -1
    for i in range(n):
        temp = 1
        for j in arr:
            temp *= j[i]
        if result < temp:
            result, r = temp, i
        elif result == temp:
            r = i
    print(r + 1)

# 왜 틀리는지 모르겠음!!!!