a = input()

while a != "#":
    iseven = a[-1]
    one = 0
    a = a[:-1]

    for i in a:
        if i == "1":
            one += 1

    if iseven == "e":
        if one % 2:
            a += "1"
        else:
            a += "0"
    else:
        if one % 2:
            a += "0"
        else:
            a += "1"
    print(a)
    a = input()