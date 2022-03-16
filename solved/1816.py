for _ in range(int(input())):
    t = int(input())
    check = True
    for i in range(2, 1000000):
        if t % i == 0:
            print("NO")
            check = False
            break
    if check:
        print("YES")