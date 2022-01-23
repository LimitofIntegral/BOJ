import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(map(int, input().split()))

count = {}
for i in arr:
    try: count[i] += 1
    except: count[i] = 1

count = dict(sorted(count.items(), reverse=True))

h = next(iter(count)) - 1
res = 0

while True:
    for i in count:
        if i > h:
            res += count[i]
        else:
            break
    
    if res >= M:
        break
    else:
        h -= 1

print(h)