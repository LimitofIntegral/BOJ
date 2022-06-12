day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for _ in range(int(input())):
    y, m = map(int, input().split())

    if m==1:
        print(y - 1, 12, day[12])
    else:
        if m==3:
            if (y%4==0 and y%100!=0) or y%400==0:
                print(y, 2, 29)
            else:
                print(y, 2, 28)
        else:
            print(y, m-1, day[m-1])