for _ in range(int(input())):
    n, d, a, b, s = map(float, input().split())
    print(f"{int(n)} {round(s * d / (a + b), 6)}")