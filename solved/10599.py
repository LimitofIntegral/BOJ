a, b, c, d = map(int, input().split())

while (a, b, c, d) != (0, 0, 0, 0):
    print(c - b, d - a)
    a, b, c, d = map(int, input().split())