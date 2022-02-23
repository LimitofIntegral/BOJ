n = int(input())

while n != 0:
    t = list(str(n))
    while len(t) != 1:
        t = list(str(sum(map(int, t))))
    print(t[0])

    n = int(input())