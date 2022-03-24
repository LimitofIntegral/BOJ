res = 1

a, b = map(int, input().split())
arr = [a // b for _ in range(b)]

i = 0

while sum(arr) < a:
    arr[i] += 1
    i += 1

for i in arr:
    res *= i

print(res)