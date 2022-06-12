a, b = map(int, input().split())
b = a * 0.01 * b
print(0 if a - b >= 100 else 1)