d = {}
arr = []

for _ in range(int(input())):
    t = tuple(map(int, input().split()))
    if t[0] not in d:
        d[t[0]] = 2
    arr.append(t)

arr.sort(key=lambda x: x[2])

for _ in range(3):
    while True:
        t = arr.pop()
        if d[t[0]]:
            d[t[0]] -= 1
            print(t[0], t[1])
            break
