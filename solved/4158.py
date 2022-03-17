import sys
input = sys.stdin.readline

a, b = map(int, input().split())

while a and b:
    count = 0
    arr1 = [int(input()) for _ in range(a)]
    arr2 = [int(input()) for _ in range(b)]

    i, j = 0, 0

    while 1:
        try:
            if arr1[i] == arr2[j]:
                count += 1
                i += 1
                j += 1
            elif arr1[i] > arr2[j]:
                j += 1
            else:
                i += 1
        except:
            break

    print(count)

    a, b = map(int, input().split())
