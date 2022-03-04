for i in range(int(input())):
    a, b = list(map(int, input().split())), list(map(int, input().split()))
    sa = a[0] * 1 + a[1] * 2 + a[2] * 3 + a[3] * 3 + a[4] * 4 + a[5] * 10
    sb = b[0] * 1 + b[1] * 2 + b[2] * 2 + b[3] * 2 + b[4] * 3 + b[5] * 5 + b[6] * 10
    
    print(f"Battle {i + 1}: ", end="")
    if sa < sb:
        print("Evil eradicates all trace of Good")
    elif sa == sb:
        print("No victor on this battle field")
    else:
        print("Good triumphs over Evil")