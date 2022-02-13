t = list(map(int, input().split()))

while True:
    for i in range(4):
        if t[i] > t[i + 1]:
            t[i], t[i + 1] = t[i + 1], t[i]
            for j in t:
                print(j, end = " ")
            print()
    if t == [1, 2, 3, 4, 5]:
        break