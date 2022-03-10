import sys
input = sys.stdin.readline
print = sys.stdout.write

d = {}

a, b = map(int, input().split())

for _ in range(a):
    s, i = input().split()
    d[s] = i

for _ in range(b):
    print(d[input().strip()] + "\n")