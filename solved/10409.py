n, t = map(int, input().split())
count = 0
arr = list(map(int, input().split()))

for i in arr:
    if i <= t:
        t -= i
        count += 1
    else:
        break

print(count)