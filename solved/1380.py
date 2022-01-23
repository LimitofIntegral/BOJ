n = int(input())
case = 1

while n != 0:
    name = {}
    number = {}
    for i in range(n):
        temp = input().rstrip()
        name[temp] = 0
        number[i + 1] = temp
    
    for i in range(2 * n - 1):
        a, b = input().split()
        name[number[int(a)]] += 1
    
    print(case, list(name.keys())[list(name.values()).index(1)])

    case += 1
    n = int(input())


"""

value값으로 key값에 접근해보기

"""