a, b, c = map(int, input().split())

p = (c - a) // b

if a + b * p == c and p >= 0:
    print(1 + p)
else:
    print("X")