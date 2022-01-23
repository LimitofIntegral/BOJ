import sys

def prime(n):
    arr = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if arr[i]:
            for j in range(2 * i, n, i):
                arr[j] = False
    
    return [i for i in range(2, n) if arr[i]]


k, l = map(int, input().split())

arr = prime(l)
check = True

for i in arr:
    if k % i == 0:
        if i >= l:
            break
        else:
            print("BAD", i)
            check = False
            break
    if k < i:
        break

if check:
    print("GOOD")