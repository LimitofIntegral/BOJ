import sys
input = sys.stdin.readline

d = {}

for _ in range(int(input())):
    a, b = input().split()
    if b == 'enter':
        d[a] = None
    else:
        del d[a]

d = sorted(d, reverse=True)

for i in d:
    print(i)