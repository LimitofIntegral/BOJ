for _ in range(int(input())):
    check = True
    n = int(input())
    a = list(map(int, input().split()))

    if n == 1:
        print("YES")
        continue
    
    for i in range(0, n - 1):
        if a[i] > a[i+1] and n - a[i] + 1 > a[i+1]:
            if i != n - 2:
                check = False
                break
            p = n - a[i + 1] + 1
            if a[i] > p and n - a[i] + 1 > p:
                check = False
                break
    
    print("YES" if check else "NO")