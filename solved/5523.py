import sys
input = sys.stdin.readline

a, b = 0, 0
for _ in range(int(input())):
    t1, t2 = map(int, input().split())
    if t1 > t2:
        a += 1
    elif t1 < t2:
        b += 1

print(a, b)