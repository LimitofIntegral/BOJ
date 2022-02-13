for _ in range(int(input())):
    a, b = map(list, input().split())
    a.reverse()
    b.reverse()
    i = 0
    result = ""
    for _ in range(min(len(a), len(b))):
        if a[i] == '0' and b[i] == '0':
            result += '0'

#일단 보류