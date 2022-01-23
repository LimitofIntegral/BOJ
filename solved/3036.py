from math import gcd

N = int(input())
arr = list(map(int, input().split()))

a = arr[0]

for i in range(len(arr) - 1):
    p = gcd(a, arr[i + 1])
    print(str(a // p) + "/" + str(arr[i + 1] // p))