result = 1

n, m = map(int, input().split())
arr = list(map(int, input().split()))

for i in arr:
    result = ((result % m) * (i % m)) % m

print(result)