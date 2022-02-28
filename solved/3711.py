import sys
input = sys.stdin.readline

for _ in range(int(input())):
    arr = []
    for _ in range(int(input())):
        arr.append(int(input()))
    c = 0
    while True:
        d = {}
        c += 1
        for i in arr:
            d[i % c] = None
        if len(arr) == len(d):
            break
    print(c)