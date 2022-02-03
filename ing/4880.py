a, b, c = map(int, input().split())

while a != 0 and b != 0 and c != 0:
    if a == 1 and b == 1 and c == 1:
        print("GP 1")
    elif b - a == c - b:
        print("AP", 2 * c - b)
    else:
        print("GP", c * (c // b))
    
    a, b, c = map(int, input().split())

    # 반례가 뭘까?