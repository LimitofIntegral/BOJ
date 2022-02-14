n, k = map(int, input().split())

k_ = (list(str(k))[-1], list(str(k * 2))[-1])

arr = []

for i in range(1, n + 1):
    if list(str(i))[-1] not in k_:
        arr.append(i)

print(len(arr))
for i in arr:
    print(i, end = " ")