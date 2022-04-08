n, m = map(int, input().split())
result = 1

for i in range(m):
    result *= (n - i)

for i in range(m):
    result //= (m - i)

print(result)