import sys
input = sys.stdin.readline

def find(x):
    if x == p[x]:
        return x
    else:
        px = find(p[x])
        p[x] = px
        return p[x]


def union(x, y):
    rx, ry = find(x), find(y)

    if rx != ry:
        p[ry] = rx
        number[rx] += number[ry]

for _ in range(int(input())):
    p = {}
    number = {}

    for _ in range(int(input())):
        x, y = input().strip().split(" ")

        if x not in p:
            p[x] = x
            number[x] = 1
        if y not in p:
            p[y] = y
            number[y] = 1
        
        union(x, y)
        print(number[find(x)])