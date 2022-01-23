import sys

def prime(n):
    arr = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if arr[i]:
            for j in range(2 * i, n, i):
                arr[j] = False
    
    return [i for i in range(2, n) if arr[i]]


p, k = map(int, input().split())

arr = prime(k)
check = True

for i in arr:
    if p % i == 0:
        print("BAD", i)
        check = False
        break
    
    if p < i:
        break

if check:
    print("GOOD")
