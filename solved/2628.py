n, m = map(int, input().split())

cut0 = [0, m]
cut1 = [0, n]

for _ in range(int(input())):
    a, b = map(int, input().split())
    if a:
        cut1.append(b)
    else:
        cut0.append(b)

cut0.sort()
cut1.sort()

result = 0

for i in range(len(cut0) - 1):
    for j in range(len(cut1) - 1):
        result = max(result, (cut0[i + 1] - cut0[i]) * (cut1[j + 1] - cut1[j]))

print(result)