import sys
input = sys.stdin.readline


def ccw(a, b, c):
    result = a[0] * b[1] + b[0] * c[1] + c[0] * a[1]
    result += (-a[1] * b[0] - b[1] * c[0] - c[1] * a[0])
    return result / 2


n = int(input())
arr = [None] * n
for i in range(n):
    a, b = map(int, input().split())
    arr[i] = (a, b)

result = 0
for i in range(1, n):
    result += ccw(arr[0], arr[i - 1], arr[i])

result = round(abs(result), 2)

print(result)
