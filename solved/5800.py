for i in range(int(input())):
    arr = sorted(list(map(int,input().split()))[1:])
    m, M = arr[0], arr[-1]
    g = 0
    for j in range(len(arr) - 1):
        g = max(g, arr[j + 1] - arr[j])
    print("Class", i + 1)
    print("Max " + str(M) + ", Min " + str(m) + ", Largest gap " + str(g))