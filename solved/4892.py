n = int(input())

case = 1
while n != 0:
    n1 = 3 * n
    print(str(case) + ".", end = " ")
    if n1 % 2:
        print("odd", end = " ")
        n2 = (n1 + 1) // 2
    else:
        print("even", end = " ")
        n2 = n1 // 2
    n3 = 3 * n2
    n4 = n3 // 9
    print(n4)

    case += 1
    n = int(input())