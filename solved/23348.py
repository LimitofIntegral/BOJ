a, b, c = map(int, input().split())
result = 0
for _ in range(int(input())):
    t = 0
    for _ in range(3):
        i, j, k = map(int, input().split())
        t += a * i + b * j + c * k
    result = max(result, t)

print(result)