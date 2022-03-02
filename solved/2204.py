n = int(input())

while n:
    arr = []
    arr_ = []
    for _ in range(n):
        t = input()
        arr.append(t)
        arr_.append(t.lower())
    arr_.sort()
    p = arr_[0]
    for i in arr:
        if i.lower() == p:
            print(i)
            break
    n = int(input())