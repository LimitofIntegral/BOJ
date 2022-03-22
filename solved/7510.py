for i in range(int(input())):
    print('Scenario #{}:'.format(i + 1))
    a = list(map(int, input().split()))
    a.sort()
    if a[0] ** 2 + a[1] ** 2 == a[2] ** 2:
        print("yes\n")
    else:
        print("no\n")