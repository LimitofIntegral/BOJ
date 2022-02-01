for _ in range(int(input())):
    n, m = map(int, input().split())
    result = 0
    for i in range(n, m + 1):
        if i % 10:
            pass
        else:
            result += 1
            t = i // 10
            while t % 10 == 0:
                result += 1
                t //= 10
    print(result)