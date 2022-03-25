for i in range(int(input())):
    a = list(map(int, input().split()))
    a.sort()
    if a[0] + a[1] <= a[2]:
        print('Case #{}: invalid!'.format(i + 1))
    else:
        if a[0] == a[1] and a[1] == a[2]:
            print('Case #{}: equilateral'.format(i + 1))
        else:
            if a[0] == a[1] or a[1] == a[2]:
                print('Case #{}: isosceles'.format(i + 1))
            else:
                print('Case #{}: scalene'.format(i + 1))
    