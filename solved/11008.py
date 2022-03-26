for _ in range(int(input())):
    s, p = input().split()
    i, j = len(s), len(p)
    c = s.count(p)
    print(i - c * j + c)