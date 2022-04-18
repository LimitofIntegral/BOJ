for _ in range(int(input())):
    n = input()
    l = len(n)
    t = str(int(n) ** 2)[-l:]
    print("YES" if n == t else "NO")