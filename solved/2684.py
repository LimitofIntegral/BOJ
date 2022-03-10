for _ in range(int(input())):
    c = [0, 0, 0, 0, 0, 0, 0, 0]
    temp = input()
    for i in range(38):
        p = temp[i:i+3]
        if p == "TTT":
            c[0] += 1
        elif p == "TTH":
            c[1] += 1
        elif p == "THT":
            c[2] += 1
        elif p == "THH":
            c[3] += 1
        elif p == "HTT":
            c[4] += 1
        elif p == "HTH":
            c[5] += 1
        elif p == "HHT":
            c[6] += 1
        else:
            c[7] += 1

    for i in c:
        print(i, end=" ")
    print()