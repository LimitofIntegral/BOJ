n = int(input())

t = int(input())

while t != 0:
    if t < n:
        print(t, "is NOT a multiple of", n, end = "")
        print('.')
    else:
        if not t % n:
            print(t, "is a multiple of", n, end = "")
            print(".")
        else:
            print(t, "is NOT a multiple of", n, end = "")
            print(".")
    
    t = int(input())