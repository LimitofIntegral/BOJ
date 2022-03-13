n, m = map(int, input().split())
a = []

for _ in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    t = list(map(int, input().split()))
    for j in range(m):
        a[i][j] += t[j]

for i in a:
    for j in i:
        print(j, end = " ")
    print()
