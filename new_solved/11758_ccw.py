x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

result = x1 * y2 + x2 * y3 + x3 * y1
result += (-y1 * x2 - y2 * x3 - y3 * x1)

if result:
    print(1 if result > 0 else -1)
else:
    print(0)
