for _ in range(int(input())):
    a, b = map(int, input().split())
    t = 2 * b - a
    print(t, b - t)