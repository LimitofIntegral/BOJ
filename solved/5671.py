while True:
    try:
        n, m = map(int, input().split())
        count = 0
        for i in range(n, m + 1):
            a = list(str(i))
            c = []
            check = True
            for j in a:
                if j not in c:
                    c.append(j)
                else:
                    check = False
                    break
            
            if check:
                count += 1
        print(count)
    except:
        break