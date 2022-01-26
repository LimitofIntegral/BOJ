x, y, w, s = map(int, input().split())

if x > y:
    x, y = y, x

if 2 * w <= s:
    print(w * (x + y))
else:
    result = 0
    result += x * s
    y -= x
    if w <= s:
        print(result + y * w)
    else:
        if y % 2:
            print(result + s * (y - 1) + w)
        else:
            print(result + s * y)