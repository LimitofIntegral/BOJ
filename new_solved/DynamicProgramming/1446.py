n, d = map(int, input().split())
way = [i for i in range(d + 1)]

short = []

for _ in range(n):
    short.append(list(map(int, input().split())))

short.sort()

step = 0
for i in short:
    s, e, w = i
    if e > d:
        continue
    while step != s:
        way[step + 1] = min(way[step + 1], way[step] + 1)
        step += 1
    way[e] = min(way[e], way[s] + w)

while step != d:
    way[step + 1] = min(way[step + 1], way[step] + 1)
    step += 1
    
print(way[-1])