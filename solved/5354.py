for _ in range(int(input())):
    n = int(input())
    a = "#" * n
    b = "#" + "J" * (n - 2) + "#"

    if n == 1:
        print("#")
        print()
    else:
        print(a)
        for _ in range(n - 2):
            print(b)
        print(a)
        print()