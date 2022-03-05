if __name__ == "__main__":
    n = int(input())
    r, i = 0, 1
    while True:
        if n >= i:
            n -= i
            i += 1
        else:
            i = 1
            n -= i
            i += 1
        r += 1
        if n == 0:
            break
    print(r)