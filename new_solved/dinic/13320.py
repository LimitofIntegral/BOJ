import random

print("502 251502")

arr = []

for i in range(1, 502):
    for j in range(i + 1, 503):
        arr.append([i, j, random.randint(1, 10000000)])
        arr.append([j, i, random.randint(1, 10000000)])

arr.sort(reverse=True)

for i in arr:
    print(*i)