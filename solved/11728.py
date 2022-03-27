n, m = map(int, input().split())

a = list(map(int, input().split()))
a.extend(map(int, input().split()))

a.sort()

for i in a:
    print(i, end = " ")
