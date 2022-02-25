d = {}
s = 0
for _ in range(10):
    m = int(input())
    s += m
    try: d[m] += 1
    except: d[m] = 1

print(int(s / 10))

t = 0
r = 0
for i in d:
    if d[i] > t:
        r = i
        t = d[i]

print(r)
