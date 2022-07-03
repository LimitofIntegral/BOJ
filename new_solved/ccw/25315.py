import sys
input = sys.stdin.readline

def ccw(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    return (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)


n = int(input())
a = []

for _ in range(n):
    sx, sy, ex, ey, w = map(int, input().split())

    a.append((w, sx, sy, ex, ey))

a.sort()
result = 0

for i in range(n - 1):
    m = 1
    for j in range(i + 1, n):
        r1 = ccw(a[i][1:3], a[i][3:], a[j][1:3]) * ccw(a[i][1:3], a[i][3:], a[j][3:])
        r2 = ccw(a[j][1:3], a[j][3:], a[i][1:3]) * ccw(a[j][1:3], a[j][3:], a[i][3:])

        if r1 < 0 and r2 < 0:
            m += 1
    result += m * a[i][0]

result += a[-1][0]
print(result)