for _ in range(int(input())):
    a, b = map(int, input().split())
    bmi = b / (a * 0.01) ** 2
    if a < 140.1:
        print(6)
    elif a < 146:
        print(5)
    elif a < 159:
        print(4)
    elif a < 161:
        if 16.0<=bmi<35:
            print(3)
        else:
            print(4)
    elif a < 204:
        if 20<=bmi<25:
            print(1)
        elif 18.5<=bmi<20 or 25<=bmi<30:
            print(2)
        elif 16<=bmi<18.5 or 30<=bmi<35:
            print(3)
        else:
            print(4)
    else:
        print(4)