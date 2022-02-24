d = {}
cnt = 0

for _ in range(int(input())):
    a, b = map(int, input().split())
    if a not in d:
        d[a] = b
    else:
        if d[a] == b:
            pass
        else:
            cnt += 1
            d[a] = b

print(cnt)